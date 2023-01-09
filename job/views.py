from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from django.core.mail import send_mail

from datetime import datetime
import datetime as dt
import requests

from job.models import *
from app_user.models import AppUser
from app_user.views import RaySendMail

#from .forms import UserForm





def IndexView(request):
    app_user = AppUser.objects.get(user__pk=request.user.id)
    jobs = Job.objects.all().order_by('-pub_date')

    job_types = set()
    countries = set()
    titles = set()
    categories = set()

    for item in jobs:
        job_types.add(item.job_type)
        countries.add(item.country)
        titles.add(item.title)
        categories.add(item.category)

    if request.method == "POST":
        location = request.POST.get("location")
        job_type = request.POST.get("job_type")
        category = request.POST.get("category")

        job = Job.objects.filter(job_type=job_type, country=location.replace("%20", " "), category=category)

        context = {"jobs": jobs,
        "job_types": job_types, "countries": countries,
        "titles": titles, "categories": categories}

        return render(request, "app_user/search_job.html", context )





    else:
        jobs = Job.objects.all().order_by('-pub_date')

        job_types = set()
        countries = set()
        titles = set()
        categories = set()

        for item in jobs:
            job_types.add(item.job_type)
            countries.add(item.country)
            titles.add(item.title)
            categories.add(item.category)



        context = {"app_user": app_user, "jobs": jobs,
        "job_types": job_types, "countries": countries,
        "titles": titles, "categories": categories}

        return render(request, "job/index.html", context )





def SearchJobView(request, query_type, query):
    app_user = AppUser.objects.get(user__pk=request.user.id)
    if request.method == "POST":
        pass


    else:

        jobs = Job.objects.all()

        job_types = set()
        countries = set()
        titles = set()
        categories = set()

        for item in jobs:
            job_types.add(item.job_type)
            countries.add(item.country)
            titles.add(item.title)
            categories.add(item.category)

        

        if query_type == "job_type":
            search_results = Job.objects.filter(job_type=query)

        elif query_type == "country":
            search_results = Job.objects.filter(country=query)

        elif query_type == "title":
            search_results = Job.objects.filter(title=query)

        elif query_type == "category":
            search_results = Job.objects.filter(category=query)

        else:
            pass


        context = {"app_user": app_user, "jobs": jobs, "search_results": search_results, 
        "job_types": job_types, "countries": countries,
        "titles": titles, "categories": categories}
        return render(request, "job/search_job.html", context )





def AllLocationView(request, query):
    app_user = AppUser.objects.get(user__pk=request.user.id)
    if request.method == "POST":
        pass


    else:

        jobs = Job.objects.all()

        job_types = set()
        countries = set()
        titles = set()
        categories = set()

        for item in jobs:
            job_types.add(item.job_type)
            countries.add(item.country)
            titles.add(item.title)
            categories.add(item.category)


        search_results = Job.objects.filter(country=query)


        context = {"app_user": app_user, "jobs": jobs, "search_results": search_results, 
        "job_types": job_types, "countries": countries,
        "titles": titles, "categories": categories}
        return render(request, "job/search_job.html", context )




#@login_required(login_url='/app/sign-in/')
def JobDetailView(request, job_id):
    try:
        app_user = AppUser.objects.get(user__pk=request.user.id)

    except:
        app_user = None

    if request.method == "POST":
        pass


    else:
        job = Job.objects.get(id=job_id)
        jobs = Job.objects.all()

        applied_status = False
        for item in job.applications.all():
            if item.app_user == app_user:
                applied_status = True

        job_types = set()
        countries = set()
        titles = set()
        categories = set()

        for item in jobs:
            job_types.add(item.job_type)
            countries.add(item.country)
            titles.add(item.title)
            categories.add(item.category)

        similar_jobs = Job.objects.filter(category=job.category)

        context = {"app_user": app_user, "job": job, "jobs": jobs, "applied_status": applied_status,
        "job_types": job_types, "countries": countries,
        "titles": titles, "categories": categories, "similar_jobs": similar_jobs}
        
        return render(request, "job/job_detail.html", context )


def AddJobFRView(request, request_id):
    app_user = AppUser.objects.get(user__pk=request.user.id)
    job_request = JobRequest.objects.get(id=request_id)
    if request.method == "POST":
        title = request.POST.get("title")
        salary = request.POST.get("salary")
        category = request.POST.get("category")
        address = request.POST.get("address")
        country = request.POST.get("country")
        description = request.POST.get("description")
        job_type = request.POST.get("job_type")
        responsibility = request.POST.get("responsibility")
        requirement = request.POST.get("requirement")
        contact_email = request.POST.get("contact_email")
        contact_phone = request.POST.get("contact_phone")
        website = request.POST.get("website")
        deadline = request.POST.get("deadline")

        job = Job.objects.create(app_user=app_user, title=title, salary=salary, category=category, address=address, country=country, description=description, job_type=job_type,
            responsibility=responsibility, requirement=requirement, contact_email=contact_email, contact_phone=contact_phone,
            deadline=deadline, website=website)
        job.save()

        job_request.job_id = job.id
        job_request.save()
        #jr = JobRequestJobConnector(job_request=job_request, job=job)
        #jr.save()

        messages.warning(request, "Job Added!")
        return HttpResponseRedirect(reverse("quiz:setup_quiz"))


    else:
        jobs = Job.objects.filter(app_user=app_user).order_by("-pub_date")

        context = {"app_user": app_user, "jobs": jobs, "job_request": job_request}
        return render(request, "job/add_job_fr.html", context )


def ApplyJobView(request, job_id, app_user_id):
    app_user = AppUser.objects.get(id=app_user_id)
    job = Job.objects.get(id=job_id)

    application = Application.objects.create(app_user=app_user)
    application.save()

    ja = JobApplicationConnector(job=job, application=application)
    ja.save()
    
    to_email = job.contact_email
    code = job.id
    subject = "Aibra Jobs: New Application!"
    message = "You have a new application for one of your jobs"
    RaySendMail(request, subject, message, to_email, code=code)

    messages.warning(request, "Job Applied!")
    return HttpResponseRedirect(reverse("quiz:take_quiz", args=[job.id,]))



    if request.method == "POST":
        pass


    else:
        job = Job.objects.get(id=job_id)
        jobs = Job.objects.all()

        context = {"app_user": app_user, "job": job, "jobs": jobs}
        return render(request, "job/apply_job.html", context )



def MyApplicationsView(request):
    app_user = AppUser.objects.get(user__pk=request.user.id)

    if request.method == "POST":
        pass


    else:
        my_applications = []
        jobs = Job.objects.all()

        for item in jobs:
            for jtem in item.applications.all():
                if jtem.app_user == app_user:
                    my_applications.append(item)

        context = {"app_user": app_user, "my_applications": my_applications}
        return render(request, "job/my_applications.html", context )






def EditJobView(request, job_id):
    job = Job.objects.get(id=job_id)
    app_user = AppUser.objects.get(user__pk=request.user.id)
    if request.method == "POST":

        title = request.POST.get("title")
        salary = request.POST.get("salary")
        address = request.POST.get("address")
        category = request.POST.get("category")
        description = request.POST.get("description")
        responsibility = request.POST.get("responsibility")
        requirement = request.POST.get("requirement")
        contact_email = request.POST.get("contact_email")
        contact_phone = request.POST.get("contact_phone")
        deadline = request.POST.get("deadline")
        qualification = request.POST.get("qualification")
        experience = request.POST.get("experience")
        website = request.POST.get("website")
        job_type = request.POST.get("job_type")
        skill_tag = request.POST.get("skill_tag")
        country = request.POST.get("country")

        job.title = title
        job.salary = salary
        job.address = address
        job.description = description
        job.responsibility = responsibility
        job.requirement = requirement
        job.contact_email = contact_email
        job.contact_phone = contact_phone
        job.deadline = deadline
        job.qualification = qualification
        job.experience = experience
        job.website = website
        job.category = category
        job.job_type = job_type
        job.skill_tag = skill_tag 
        job.country = country
        job.save()

        messages.warning(request, "Job Updated!")
        return HttpResponseRedirect(reverse("job:add_job"))


    else:
        jobs = Job.objects.filter(app_user=app_user)
        
        context = {"app_user": app_user, "jobs": jobs, "job": job}
        return render(request, "job/edit_job.html", context )



def AddJobView(request):
    app_user = AppUser.objects.get(user__pk=request.user.id)
    app_users = AppUser.objects.all()
    if request.method == "POST":
        title = request.POST.get("title")
        salary = request.POST.get("salary")
        category = request.POST.get("category")
        address = request.POST.get("address")
        country = request.POST.get("country")
        description = request.POST.get("description")
        job_type = request.POST.get("job_type")
        responsibility = request.POST.get("responsibility")
        requirement = request.POST.get("requirement")
        contact_email = request.POST.get("contact_email")
        contact_phone = request.POST.get("contact_phone")
        deadline = request.POST.get("deadline")
        qualification = request.POST.get("qualification")
        experience = request.POST.get("experience")
        skill_tag = request.POST.get("skill_tag")

        job = Job.objects.create(app_user=app_user, title=title, salary=salary, category=category, address=address, country=country, description=description, job_type=job_type,
            responsibility=responsibility, requirement=requirement, contact_email=contact_email, contact_phone=contact_phone,
            deadline=deadline, experience=experience, qualification=qualification, skill_tag=skill_tag)
        job.save()
        
        for item in app_users[8:9]:
            subject = "Aibra Jobs: New Job Alert!"
            message = title +": " + description[:200]
            to_email = item.user.username
            code = job.id
            RaySendMail(request, subject, message, to_email, code=code)

        messages.warning(request, "Job Added!")
        return HttpResponseRedirect(reverse("quiz:setup_quiz"))


    else:
        jobs = Job.objects.filter(app_user=app_user)

        context = {"app_user": app_user, "jobs": jobs}
        return render(request, "job/add_job.html", context )




def ManageJobView(request):
    app_user = AppUser.objects.get(user__pk=request.user.id)
    app_users = AppUser.objects.all()
    if request.method == "POST":
        pass

    else:
        jobs = Job.objects.filter(app_user=app_user)

        context = {"app_user": app_user, "jobs": jobs}
        return render(request, "job/manage_job.html", context)


def JobApplicationsView(request, job_id):
    app_user = AppUser.objects.get(user__pk=request.user.id)
    if request.method == "POST":
        pass


    else:
        job = Job.objects.get(id=job_id)

        applications = job.applications.all()

        context = {"app_user": app_user, "job": job, "applications": applications}
        return render(request, "job/job_applications.html", context )


def RequestView(request):
    app_user = AppUser.objects.get(user__pk=request.user.id)
    if request.method == "POST":
        title = request.POST.get("title")
        category = request.POST.get("category")
        salary = request.POST.get("salary")
        description = request.POST.get("description")
        job_type = request.POST.get("job_type")
        slots = request.POST.get("slots")
        website = request.POST.get("website")
        address = request.POST.get("address")
        deadline = request.POST.get("deadline")
        experience = request.POST.get("experience")
        website = request.POST.get("website")

        job_request = JobRequest.objects.create(app_user=app_user, title=title, salary=salary,
        description=description, job_type=job_type, slots=slots,
            deadline=deadline, category=category, website=website, address=address, experience=experience)
        job_request.save()

        messages.warning(request, "Request Created!")
        return HttpResponseRedirect(reverse("job:assign", args=[job_request.id,]))


    else:
        all_requests = JobRequest.objects.filter(app_user=app_user)
        context = {"app_user": app_user, "all_requests": all_requests}
        return render(request, "job/request.html", context )



def AssignView(request, request_id):
    app_user = AppUser.objects.get(user__pk=request.user.id)
    job_request = JobRequest.objects.get(id=request_id)
    if request.method == "POST":
        query_price = request.POST.get("query_price")

        query_star5 = request.POST.get("query_star5")
        query_star4 = request.POST.get("query_star4")
        query_star3 = request.POST.get("query_star3")
        query_star2 = request.POST.get("query_star2")
        query_star1 = request.POST.get("query_star1")
        query_star0 = request.POST.get("query_star0")

        query_star = []
        if query_star0:
            query_star.append(0)
        if query_star1:
            query_star.append(1)
        if query_star2:
            query_star.append(2)
        if query_star3:
            query_star.append(3)
        if query_star4:
            query_star.append(4)
        if query_star5:
            query_star.append(4)

        if len(query_star) == 0:
            query_star.append(1)

        query_location = request.POST.get("query_location")

    
        #result = {"query_price": query_price, "query_star5": query_star5,
        #"query_star4": query_star4, "query_star3": query_star3, "query_star2": query_star2,
        #"query_star1": query_star1, "query_location": query_location,
        #}

        all_recruiters = []
        
        for item in query_star:
            if query_location == "global":
                all_recruiters_j = AppUser.objects.filter(account_type="recruiter", rank=str(item))
                for jtem in all_recruiters_j:
                    if int(jtem.charge) > int(query_price) or int(jtem.charge) == int(query_price):
                        all_recruiters.append(jtem)
            else:
                all_recruiters_j = AppUser.objects.filter(account_type="recruiter", rank=str(item), country=query_location)
                for jtem in all_recruiters_j:
                    if int(jtem.charge) > int(query_price) or int(jtem.charge) == int(query_price):
                        all_recruiters.append(jtem)
        all_recruiters = set(all_recruiters)

        locations = set([item.country for item in AppUser.objects.all()])
        
        context = {"app_user": app_user, "all_recruiters": all_recruiters,
        "request_id": request_id, "locations": locations}
        return render(request, "job/assign.html", context)

        #recruiter = request.POST.get("recruiter")

        #messages.warning(request, "Request Created!")
        #return HttpResponseRedirect(reverse("job:assign2", args=[request_id, recruiter]))


    else:
        locations = set([item.country for item in AppUser.objects.all()])
        
        all_recruiters = AppUser.objects.filter(account_type="recruiter")
        context = {"app_user": app_user, "all_recruiters": all_recruiters,
        "request_id": request_id, "locations": locations}
        return render(request, "job/assign.html", context)



def Assign2View(request, request_id, recruiter):
    app_user = AppUser.objects.get(user__pk=request.user.id)
    recruiter = AppUser.objects.get(user__username=recruiter)

    job_request = JobRequest.objects.get(id=request_id)
    if request.method == "POST":
        
        bep_balance = requests.get("https://api.iotexchartapp.com/aibra/get-balance/%s/" % (app_user.wallet_address)).json()

        #return HttpResponse(str(float(bep_balance["data"][0]["balance"])))
        if float(float(bep_balance["data"][0]["balance"])) > float(recruiter.charge):
            
            sender = app_user.wallet_address
            sender_key = app_user.wallet_key
            receiver1 = recruiter.wallet_address
            receiver2 = "0xbCA60DDe596B82a4Cb8CC3233BF8f0ED09280557"
            amount1 = float(recruiter.charge) - (float(recruiter.charge)*0.1)
            amount2 = float(recruiter.charge)*0.1
            token = "abr"
        
            try:
                resp1 = requests.post("https://api.iotexchartapp.com/send-brise/",
                data={"sender":sender,"sender_key":sender_key, "receiver": receiver1,
                "amount":amount1, "token":token}).json()
    
                txn_hash1 = resp1["txn_hash"]
    
                #import time
                #time.sleep(5)
    
                #resp2 = requests.post("https://api.iotexchartapp.com/send-brise/",
                #data={"sender":sender,"sender_key":sender_key, "receiver": receiver2,
                #"amount":amount2, "token":token}).json()
    
                #txn_hash2 = resp2["txn_hash"]
                

            except:
                txn_hash1 = None
            #    txn_hash2 = None

            if txn_hash1 != None:
                job_request.recruiter = recruiter.user.username
                job_request.save()
                
                RaySendMail(request, "Candidate Request", "You just received payment from a Company to sort for candidates. Kindly check your profile", recruiter.user.username)

                messages.warning(request, "Request Created!")
                return HttpResponseRedirect(reverse("job:request"))
            else:
                messages.warning(request, "Sorry, something went wrong.")
                return HttpResponseRedirect(reverse("job:assign2", args=[job_request.id, recruiter.user.username,]))

        else:
            messages.warning(request, "Sorry, something went wrong..")
            return HttpResponseRedirect(reverse("job:assign2", args=[job_request.id, recruiter.user.username,]))


    else:
        locations = set([item.country for item in AppUser.objects.all()])
        all_recruiters = AppUser.objects.filter(account_type="recruiter")
        context = {"app_user": app_user, "recruiter": recruiter, "locations": locations}
        return render(request, "job/assign2.html", context )



def EditRequestView(request, request_id):
    app_user = AppUser.objects.get(user__pk=request.user.id)
    job_request = JobRequest.objects.get(id=request_id)
    if request.method == "POST":
        title = request.POST.get("title")
        salary = request.POST.get("salary")
        description = request.POST.get("description")
        job_type = request.POST.get("job_type")
        slots = request.POST.get("slots")
        deadline = request.POST.get("deadline")

        job_request.title = title
        job_request.salary = salary
        job_request.description = description
        job_request.job_type = job_type
        job_request.slots = slots
        job_request.deadline = deadline

        job_request.save()

        messages.warning(request, "Request Updated!")
        return HttpResponseRedirect(reverse("job:edit_request", args=[request_id,]))

    else:
        

        context = {"app_user": app_user, "job_request": job_request}
        return render(request, "job/edit_request.html", context )


def RequestDetailView(request, request_id):
    try:
        app_user = AppUser.objects.get(user__pk=request.user.id)
        job_request = JobRequest.objects.get(id=request_id)
        job = Job.objects.get(id=job_request.job_id)
    
        if request.method == "POST":
            rank = int(request.POST.get("rank"))
            recruiter = job.app_user
    
            #return HttpResponse(str(recruiter.rankers))
            #recruiter.rank = 1
            #recruiter.ranks = 1
            #recruiter.rankers = 1
            recruiter.ranks = float((float(recruiter.ranks)+ float(rank)))
            recruiter.rankers = float(float(recruiter.rankers) + float(1))
            recruiter.rank = int(float(float(recruiter.ranks)/float(recruiter.rankers)))
            recruiter.save()
    
            #return HttpResponse(str(recruiter.rankers))
    
            messages.warning(request, "Ranking successful...")
            return HttpResponseRedirect(reverse("job:request_detail", args=[request_id,]))
    
        else:
            
    
            context = {"app_user": app_user, "job_request": job_request, "job": job}
            return render(request, "job/request_detail.html", context )

    except:
        messages.warning(request, "Sorry, no applications yet1")
        return HttpResponseRedirect(reverse("job:request"))        


def AllRequestsView(request):
    app_user = AppUser.objects.get(user__pk=request.user.id)
    if request.method == "POST":
        pass


    else:
        all_requests = JobRequest.objects.filter(recruiter=app_user.user.username).order_by("-pub_date")

        context = {"app_user": app_user, "all_requests": all_requests}
        return render(request, "job/all_requests.html", context )

def error_404(request, exception):
	return render(request,'app_user/404.html')

def error_500(request):
	return render(request,'app_user/500.html')