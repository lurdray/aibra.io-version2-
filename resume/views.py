from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User

from django.core.mail import send_mail

from datetime import datetime
import datetime as dt
import requests
from django.utils import timezone

from app_user.models import AppUser
from resume.models import *



def IndexView(request):
    if request.method == "POST":
        pass


    else:

        app_user = AppUser.objects.get(user__pk=request.user.id)
        
        
        
        if app_user:
            import qrcode
            from io import BytesIO
            from django.core.files import File
            from PIL import Image, ImageDraw
        
            QRcode = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
            url = 'https://app.aibra.io/app/%s/' % (app_user.wallet_address)
            QRcode.add_data(url)
            QRimg = QRcode.make_image()
        
            canvas = Image.new('RGB', (550,550), 'white')
            draw = ImageDraw.Draw(canvas)
            canvas.paste(QRimg)
            fname = f'%s.png' % (app_user.wallet_address)
            buffer = BytesIO()
            canvas.save(buffer,'PNG')
            app_user.qr_photo.save(fname, File(buffer), save=False)
            app_user.save()
            canvas.close()


        context = {"app_user": app_user, "careers": app_user.resume.careers, "title":app_user.resume.titles, "opening_statements": app_user.resume.opening_statements,
        "educations": app_user.resume.educations, "skills": app_user.resume.skills, "projects": app_user.resume.projects, "awards": app_user.resume.awards}
        return render(request, "resume/index.html", context )



def UpdateResume1View(request):
    if request.method == "POST":
        app_user = AppUser.objects.get(user__pk=request.user.id)

        title_obj = request.POST.get("title")
        opening_statement_obj = request.POST.get("opening_statement")



        if app_user.resume.titles.first():
            title = app_user.resume.titles.first()
            title.title = title_obj

        else:
            title = Title.objects.create(title=title_obj, status=True)

        title.save()


        if app_user.resume.opening_statements.first():
            opening_statement = app_user.resume.opening_statements.first()
            opening_statement.opening_statement = opening_statement_obj

        else:
            opening_statement = OpeningStatement.objects.create(opening_statement=opening_statement_obj, status=True)
        
        opening_statement.save()


        rt = ResumeTitleConnector(resume=app_user.resume, title=title)
        rt.save()
        ro = ResumeOpeningStatementConnector(resume=app_user.resume, opening_statement=opening_statement)
        ro.save()

        
        if app_user.resume.resume_status == False:
            app_user.resume.resume_status = True
            app_user.resume.resume_cent = 20
            app_user.save()
            
        messages.warning(request, "Welldone! Resume Updated successfully!")
        return HttpResponseRedirect(reverse("resume:update_resume2"))


    else:
        app_user = AppUser.objects.get(user__pk=request.user.id)

        context = {"app_user": app_user, "title": app_user.resume.titles.first(), "opening_statement": app_user.resume.opening_statements.first()}
        return render(request, "resume/update_resume1.html", context )



def EditResume2View(request, work_experience_id):
    work_experience = WorkExperience.objects.get(id=work_experience_id)

    if request.method == "POST":
        app_user = AppUser.objects.get(user__pk=request.user.id)

        work_experience_obj = request.POST.get("work_experience")
        company = request.POST.get("company")
        detail = request.POST.get("detail")
        date_from = request.POST.get("date_from")
        date_to = request.POST.get("date_to")

        work_experience.work_experience = work_experience_obj
        work_experience.company = company
        work_experience.detail = detail
        work_experience.date_from = date_from
        work_experience.date_to = date_to
        work_experience.save()
            
        messages.warning(request, "Welldone! Resume Updated successfully!")
        return HttpResponseRedirect(reverse("resume:index"))



    else:
        app_user = AppUser.objects.get(user__pk=request.user.id)

        context = {"app_user": app_user,"work_experience": work_experience}
        return render(request, "resume/edit_resume2.html", context )





def UpdateResume2View(request):
    if request.method == "POST":
        app_user = AppUser.objects.get(user__pk=request.user.id)

        work_experience = request.POST.get("work_experience")
        company = request.POST.get("company")
        detail = request.POST.get("detail")
        date_from = request.POST.get("date_from")
        date_to = request.POST.get("date_to")

        current_date = request.POST.get("current_date")
        
        if str(current_date) == "on":
            date_to = "Currently works here!"
            
        #return HttpResponse(str(date_to))
        work_experience = WorkExperience.objects.create(work_experience=work_experience, company=company, detail=detail, date_from=date_from, date_to=date_to, status=True)
        work_experience.save()

        rw = ResumeWorkExperienceConnector(resume=app_user.resume, work_experience=work_experience)
        rw.save()

        if app_user.resume.work_experience_status == False:
            app_user.resume.work_experience_status = True
            app_user.resume.resume_cent = 40
            app_user.save()
            
        messages.warning(request, "Welldone! Resume Updated successfully!")
        return HttpResponseRedirect(reverse("resume:add_career"))



    else:
        app_user = AppUser.objects.get(user__pk=request.user.id)

        context = {"app_user": app_user}
        return render(request, "resume/update_resume2.html", context )



def UpdateResume3View(request):
    if request.method == "POST":
        pass


    else:
        app_user = AppUser.objects.get(user__pk=request.user.id)

        context = {"app_user": app_user, "careers": app_user.resume.careers,
        "educations": app_user.resume.educations, "skills": app_user.resume.skills}
        return render(request, "resume/add_career.html", context )



def EditCareerView(request, career_id):
    career = Career.objects.get(id=career_id)
    if request.method == "POST":
        app_user = AppUser.objects.get(user__pk=request.user.id)

        career_obj = request.POST.get("career")
        detail = request.POST.get("detail")
        date_from = request.POST.get("date_from")
        date_to = request.POST.get("date_to")

        career.career = career_obj
        career.detail = detail
        career.date_from = date_from
        career.date_to =date_to
        career.save()
            
        messages.warning(request, "Welldone! Resume Updated successfully!")
        return HttpResponseRedirect(reverse("resume:index"))



    else:
        app_user = AppUser.objects.get(user__pk=request.user.id)

        context = {"app_user": app_user, "career": career}
        return render(request, "resume/edit_career.html", context )



def AddCareerView(request):

    if request.method == "POST":
        app_user = AppUser.objects.get(user__pk=request.user.id)

        career = request.POST.get("career")
        detail = request.POST.get("detail")
        date_from = request.POST.get("date_from")
        date_to = request.POST.get("date_to")
        
        current_date = request.POST.get("current_date")
        
        if str(current_date) == "on":
            date_to = "present!"

        career = Career.objects.create(career=career, detail=detail, date_from=date_from, date_to=date_to, status=True)
        career.save()

        rc = ResumeCareerConnector(resume=app_user.resume, career=career)
        rc.save()

            
        messages.warning(request, "Welldone! Resume Updated successfully!")
        return HttpResponseRedirect(reverse("resume:add_education"))



    else:
        app_user = AppUser.objects.get(user__pk=request.user.id)

        context = {"app_user": app_user}
        return render(request, "resume/add_career.html", context )




def EditEducationView(request, education_id):
    education = Education.objects.get(id=education_id)
    if request.method == "POST":
        app_user = AppUser.objects.get(user__pk=request.user.id)

        education_obj = request.POST.get("education")
        education_detail = request.POST.get("course")
        education_institution = request.POST.get("institution")
        date_from = request.POST.get("date_from")
        date_to = request.POST.get("date_to")

        education.education = education_obj
        education.detail = education_detail
        education_institution = education_institution
        education.date_from = date_from
        education.date_to = date_to
        education.save()
            
        messages.warning(request, "Welldone! Resume Updated successfully!")
        return HttpResponseRedirect(reverse("resume:index"))



    else:
        app_user = AppUser.objects.get(user__pk=request.user.id)

        context = {"app_user": app_user, "education": education}
        return render(request, "resume/edit_education.html", context )



def AddEducationView(request):

    if request.method == "POST":
        app_user = AppUser.objects.get(user__pk=request.user.id)

        education = request.POST.get("education")
        date_from = request.POST.get("date_from")
        date_to = request.POST.get("date_to")
        course = request.POST.get("course")
        institution = request.POST.get("institution")

        current_date = request.POST.get("current_date")
        
        if str(current_date) == "on":
            date_to = "still a student"

        education = Education.objects.create(education=education, date_from=date_from, date_to=date_to, course=course, institution=institution, status=True)
        education.save()

        rc = ResumeEducationConnector(resume=app_user.resume, education=education)
        rc.save()

            
        messages.warning(request, "Welldone! Resume Updated successfully!")
        return HttpResponseRedirect(reverse("resume:add_skill"))



    else:
        app_user = AppUser.objects.get(user__pk=request.user.id)

        context = {"app_user": app_user}
        return render(request, "resume/add_education.html", context )



def EditSkillView(request, skill_id):
    skill = Skill.objects.get(id=skill_id)
    if request.method == "POST":
        app_user = AppUser.objects.get(user__pk=request.user.id)

        skill_obj = request.POST.get("skill")
        detail = request.POST.get("detail")
        date_from = request.POST.get("date_from")
        date_to = request.POST.get("date_to")

        skill.skill = skill_obj
        skill.detail = detail
        skill.date_from = date_from
        skill.date_to = date_to
        skill.save()

        messages.warning(request, "Welldone! Resume Updated successfully!")
        return HttpResponseRedirect(reverse("resume:index"))



    else:
        app_user = AppUser.objects.get(user__pk=request.user.id)

        context = {"app_user": app_user, "skill": skill}
        return render(request, "resume/edit_skill.html", context )





def AddSkillView(request):

    if request.method == "POST":
        app_user = AppUser.objects.get(user__pk=request.user.id)

        skill = request.POST.get("skill")
        detail = request.POST.get("detail")
        date_from = request.POST.get("date_from")
        date_to = request.POST.get("date_to")

        skill = Skill.objects.create(skill=skill, detail=detail, date_from=date_from, date_to=date_to, status=True)
        skill.save()

        rs = ResumeSkillConnector(resume=app_user.resume, skill=skill)
        rs.save()

        messages.warning(request, "Welldone! Resume Updated successfully!")
        return HttpResponseRedirect(reverse("resume:add_project"))



    else:
        app_user = AppUser.objects.get(user__pk=request.user.id)

        context = {"app_user": app_user}
        return render(request, "resume/add_skill.html", context )





def EditProjectView(request, project_id):
    project = Project.objects.get(id=project_id)
    if request.method == "POST":
        app_user = AppUser.objects.get(user__pk=request.user.id)

        project_obj = request.POST.get("project")
        detail = request.POST.get("detail")
        link = request.POST.get("link")

        project.project = project_obj
        project.detail = detail
        project.link = link
        project.save()

        messages.warning(request, "Welldone! Resume Updated successfully!")
        return HttpResponseRedirect(reverse("resume:index"))



    else:
        app_user = AppUser.objects.get(user__pk=request.user.id)

        context = {"app_user": app_user, "project": project}
        return render(request, "resume/edit_project.html", context )


def AddProjectView(request):

    if request.method == "POST":
        app_user = AppUser.objects.get(user__pk=request.user.id)

        project = request.POST.get("project")
        detail = request.POST.get("detail")
        link = request.POST.get("link")

        project = Project.objects.create(project=project, detail=detail, link=link, status=True)
        project.save()

        rp = ResumeProjectConnector(resume=app_user.resume, project=project)
        rp.save()

        messages.warning(request, "Welldone! Resume Updated successfully!")
        return HttpResponseRedirect(reverse("resume:add_hobby"))



    else:
        app_user = AppUser.objects.get(user__pk=request.user.id)

        context = {"app_user": app_user}
        return render(request, "resume/add_project.html", context )



def EditHobbyView(request, hobby_id):
    hobby = Hobby.objects.get(id=hobby_id)
    if request.method == "POST":
        app_user = AppUser.objects.get(user__pk=request.user.id)

        hobby_obj = request.POST.get("hobby")
        hobby.hobby = hobby_obj
        hobby.save()

        messages.warning(request, "Welldone! Resume Updated successfully!")
        return HttpResponseRedirect(reverse("resume:index"))



    else:
        app_user = AppUser.objects.get(user__pk=request.user.id)

        context = {"app_user": app_user, "hobby": hobby}
        return render(request, "resume/edit_hobby.html", context )


def AddHobbyView(request):
    if request.method == "POST":
        app_user = AppUser.objects.get(user__pk=request.user.id)

        hobby = request.POST.get("hobby")

        hobby = Hobby.objects.create(hobby=hobby, status=True)
        hobby.save()

        rh = ResumeHobbyConnector(resume=app_user.resume, hobby=hobby)
        rh.save()

        messages.warning(request, "Welldone! Resume Updated successfully!")
        return HttpResponseRedirect(reverse("resume:add_award"))



    else:
        app_user = AppUser.objects.get(user__pk=request.user.id)

        context = {"app_user": app_user}
        return render(request, "resume/add_hobby.html", context )



def EditAwardView(request, award_id):
    award = Award.objects.get(id=award_id)
    if request.method == "POST":
        app_user = AppUser.objects.get(user__pk=request.user.id)

        award_obj = request.POST.get("award")
        detail = request.POST.get("detail")
        year = request.POST.get("year")
        link = request.POST.get("link")

        award.award = award_obj
        award.detail = detail
        award.year = year
        award.link = link
        award.save()

        messages.warning(request, "Welldone! Resume Updated successfully!")
        return HttpResponseRedirect(reverse("resume:index"))



    else:
        app_user = AppUser.objects.get(user__pk=request.user.id)

        context = {"app_user": app_user, "award": award}
        return render(request, "resume/edit_award.html", context )



def AddAwardView(request):

    if request.method == "POST":
        app_user = AppUser.objects.get(user__pk=request.user.id)

        award = request.POST.get("award")
        detail = request.POST.get("detail")
        year = request.POST.get("year")
        link = request.POST.get("link")

        award = Award.objects.create(award=award, detail=detail, year=year, link=link, status=True)
        award.save()

        ra = ResumeAwardConnector(resume=app_user.resume, award=award)
        ra.save()

        messages.warning(request, "Welldone! Resume Updated successfully!")
        return HttpResponseRedirect(reverse("resume:index"))



    else:
        app_user = AppUser.objects.get(user__pk=request.user.id)

        context = {"app_user": app_user}
        return render(request, "resume/add_award.html", context )


def EditRefereeView(request, referee_id):
    referee = Referee.objects.get(id=referee_id)
    if request.method == "POST":
        app_user = AppUser.objects.get(user__pk=request.user.id)

        referee_obj = request.POST.get("referee")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        place_of_work = request.POST.get("place_of_work")

        referee.referee = referee_obj
        referee.phone = phone
        referee.email = email
        referee.place_of_work = place_of_work
        referee.save()

        messages.warning(request, "Welldone! Resume Updated successfully!")
        return HttpResponseRedirect(reverse("resume:update_resume4"))



    else:
        app_user = AppUser.objects.get(user__pk=request.user.id)

        context = {"app_user": app_user, "referee": referee}
        return render(request, "resume/edit_referee.html", context )

def AddRefereeView(request):

    if request.method == "POST":
        app_user = AppUser.objects.get(user__pk=request.user.id)

        referee = request.POST.get("referee")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        place_of_work = request.POST.get("place_of_work")

        referee = Referee.objects.create(referee=referee, email=email, phone_no=phone, place_of_work=place_of_work, status=True)
        referee.save()

        rr = ResumeRefereeConnector(resume=app_user.resume, referee=referee)
        rr.save()

        messages.warning(request, "Welldone! Resume Updated successfully!")
        return HttpResponseRedirect(reverse("resume:update_resume4"))



    else:
        app_user = AppUser.objects.get(user__pk=request.user.id)

        context = {"app_user": app_user}
        return render(request, "resume/add_referee.html", context )



def UpdateResume4View(request):
    if request.method == "POST":
        pass


    else:
        app_user = AppUser.objects.get(user__pk=request.user.id)

        context = {"app_user": app_user, "careers": app_user.resume.careers,
        "educations": app_user.resume.educations,  "hobbies":app_user.resume.hobbies, "referees":app_user.resume.referees, "skills": app_user.resume.skills, "projects": app_user.resume.projects, "awards": app_user.resume.awards}
        return render(request, "resume/update_resume4.html", context )



def UpdateResume5View(request):
    if request.method == "POST":
        pass


    else:
        app_user = AppUser.objects.get(user__pk=request.user.id)

        context = {"app_user": app_user, "careers": app_user.resume.careers,
        "educations": app_user.resume.educations, "skills": app_user.resume.skills, "projects": app_user.resume.projects, "awards": app_user.resume.awards}
        return render(request, "resume/update_resume5.html", context )

def error_404(request, exception):
	return render(request,'app_user/404.html')
	
def error_500(request):
	return render(request,'app_user/500.html')