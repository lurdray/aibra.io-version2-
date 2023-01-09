from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User

from django.core.mail import send_mail
from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from datetime import datetime
import datetime as dt
import requests

from .forms import UserForm
from .models import AppUser
from resume.models import Resume
from django.contrib.auth.decorators import login_required

import random
import string
from job.models import Job

def ray_randomiser(length=6):
    landd = string.ascii_letters + string.digits
    return ''.join((random.choice(landd) for i in range(length)))
    

def RaySendMail(request, subject, message, to_email, code=None):

    try:
        context = {"subject": subject, "message": message, "code": code}
        html_message = render_to_string('app_user/message.html', context)
        message = strip_tags(message)

        send_mail(
            subject,
            message,
            'admin@aibra.io',
            [to_email,],
            html_message=html_message,
            fail_silently=False,
        )

    except:
        pass




def ForgotPasswordView(request):
    
    if request.method == "POST":
        email = request.POST.get("username")
        
        app_users = AppUser.objects.filter(user__username=email)
        
        if len(app_users) > 0:
            app_user = app_users.last()
            app_user.otp_code = ray_randomiser()
            app_user.save()
            
            RaySendMail(request, subject="Password Reset.", message="Looks like you lost your password. Kindly use this OTP code; %s to retrieve your account." % (app_user.otp_code), to_email=app_user.user.username, code=app_user.otp_code)

        
            messages.warning(request, "Set new password.")
            return HttpResponseRedirect(reverse("app_user:set_new_p"))
        
        else:
            messages.warning(request, "Sorry, Invalid OTP code.")
            return HttpResponseRedirect(reverse("app_user:forgot_password"))
        
        
    else:
        
        context = {}
        return render(request, "app_user/forgot_password.html", context)
        
        



def SetNewPView(request):
    app_user = AppUser.objects.get(user__pk=request.user.id)
    if request.method == "POST":
        otp = request.POST.get("otp")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        
        app_users = AppUser.objects.filter(otp_code=otp)
        
        if request.POST.get("password2") != request.POST.get("password1"):
            messages.warning(request, "Make sure both passwords match")
            return HttpResponseRedirect(reverse("app_user:set_new_p"))
            
        elif len(app_users) > 0:
            app_user = app_users.last()
            
            user = app_user.user
            user.set_password(str(password2))
            user.save()
        
            messages.warning(request, "New Password Created!")
            return HttpResponseRedirect(reverse("app_user:sign_in"))
            
        else:
            messages.warning(request, "Sorry, Invalid OTP code.")
            return HttpResponseRedirect(reverse("app_user:set_new_p"))
        
        
    else:
        context = {"app_user":app_user}
        return render(request, "app_user/set_new_p.html", context)
        
        
                

def SignInView(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)

                app_user = AppUser.objects.get(user__pk=request.user.id)
                
                if app_user.ec_status == True:
                    
                    if app_user.user.username == "odiagaraymondrayray@gmail.com":
                
                        print("11111111111111111111111111111111")
                        messages.success(request, "Welcome Onboard")
                        return HttpResponseRedirect(reverse("admin_app:index"))
                    
                    else:
                        print("22222222222222222222222222222222")
                        messages.warning(request, "Welcome Onboard")
                        return HttpResponseRedirect(reverse("app_user:update_appuser"))
                
                
                else:
                    print("22222222222222222222222222222222")
                    messages.warning(request, "Sorry, validate your account")
                    return HttpResponseRedirect(reverse("app_user:sign_in"))
                
            else:
                print("22222222222222222222222222222222")
                messages.warning(request, "Sorry, Invalid Login Details")
                return HttpResponseRedirect(reverse("app_user:sign_in"))

        else:
            print("33333333333333333333333333333333333333")
            messages.warning(request, "Sorry, Invalid Login Details")
            return HttpResponseRedirect(reverse("app_user:sign_in"))

    else:
        context = {}
        return render(request, "app_user/sign_in.html", context )




def SignUpView(request):
    if request.method == "POST":

        form = UserForm(request.POST or None, request.FILES or None)
        email = request.POST.get("username")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        account_type = request.POST.get("account_type")


        if request.POST.get("password2") != request.POST.get("password1"):
            messages.warning(request, "Make sure both passwords match")
            return HttpResponseRedirect(reverse("app_user:sign_up"))

            
        else:
            try:
                AppUser.objects.get(user__email=request.POST.get("username"))
                messages.warning(request, "Email Address already taken!")
                return HttpResponseRedirect(reverse("app_user:sign_up"))


            except:
                user = form.save()
                user.set_password(request.POST.get("password1"))
                user.save()

                app_user = AppUser.objects.create(user=user, account_type=account_type)
                app_user.otp_code = ray_randomiser()

                resume = Resume.objects.create()
                resume.save

                app_user.resume = resume
                
                app_user.save()

                user = app_user.user
                user.email = email
                
                user.save()
                
                RaySendMail(request, subject="Email Confirmation.", message="Thank you for signing up with Aibra, Your OTP code is %s" % (app_user.otp_code), to_email=app_user.user.username, code=app_user.otp_code)

                if user:
                    if user.is_active:
                        login(request, user)

                        app_user = AppUser.objects.get(user__pk=request.user.id)
                        messages.warning(request, "An OTP code has been sent to your email")
                        return HttpResponseRedirect(reverse("app_user:complete_sign_up"))

    else:
        form = UserForm()
        context = {"form": form}
        return render(request, "app_user/sign_up.html", context )



    return render(request, "app_user/sign_up.html", context )



def SignUpView2(request):
    if request.method == "POST":

        wallet_address = request.POST.get("wallet_address")

        if wallet_address == "none":
            messages.warning(request, "Sorry, connect to metamask first.")
            return HttpResponseRedirect(reverse("app_user:sign_up"))

            
        else:
            otp_code = ray_randomiser()

            try:
                user = User.objects.get(username=wallet_address)
                
            except:
                user = User.objects.create(username=wallet_address)
                user.set_password(otp_code)
                user.save()
                

            try:
                app_user = AppUser.objects.get(wallet_address=wallet_address)
                
            except:
                app_user = AppUser.objects.create(user=user, wallet_address=wallet_address, account_type="candidate")
                app_user.otp_code = otp_code
                app_user.ec_status = True
                app_user.status = True

                resume = Resume.objects.create()
                resume.save

                app_user.resume = resume

            app_user.save()

            user = app_user.user
            user.email = wallet_address
            
            user.save()

            if user:
                if user.is_active:
                    login(request, user)

            messages.warning(request, "Welcome onboard.")
            return HttpResponseRedirect(reverse("job:index"))


    else:
        form = UserForm()
        context = {"form": form}
        return render(request, "app_user/sign_up2.html", context )

        
def CompleteSignUpView(request):
    app_user = AppUser.objects.get(user__pk=request.user.id)
    if request.method == "POST":
        otp = request.POST.get("otp")
        
        
        if otp == app_user.otp_code:
            app_user.ec_status = True
            app_user.save()

            messages.warning(request, "Welcome Onboard!")
            return HttpResponseRedirect(reverse("app_user:app"))

        else:
            messages.warning(request, "Sorry, Invalid OTP Code.")
            return HttpResponseRedirect(reverse("app_user:complete_sign_up"))


    else:
        context = {}
        return render(request, "app_user/complete_sign_up.html", context )





def SignOutView(request):

    logout(request)
    return HttpResponseRedirect(reverse("app_user:sign_in"))


def AppView(request):
    #app_user = AppUser.objects.get(user__pk=request.user.id)
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

        context = {"jobs": jobs,
        "job_types": job_types, "countries": countries,
        "titles": titles, "categories": categories}

        return render(request, "app_user/app2.html", context )


def UpdateAppuserView(request):
    app_user = AppUser.objects.get(user__pk=request.user.id)
    if request.method == "POST":
        try:
            profile_photo = request.FILES["profile_photo"]
        except:
            profile_photo = app_user.profile_photo	

        try:
            cv = request.FILES["cv"]
        except:
            cv = app_user.cv	

        try:
            agency_name = request.POST.get("agency_name")
        except:
            agency_name = app_user.agency_name
            
        try:
            bio = request.POST.get("bio")
        except:
            bio = app_user.bio

        try:
            charge = request.POST.get("charge")
        except:
            charge = app_user.charge

        try:
            agency_logo = request.FILES["agency_logo"]
        except:
            agency_logo = app_user.agency_logo


        app_user.cv = cv
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        age = request.POST.get("age")
        gender = request.POST.get("gender")
        phone = request.POST.get("phone")
        address = request.POST.get("address")
        country = request.POST.get("country")

        postcode = request.POST.get("postcode")
        language = request.POST.get("language")
        job_category = request.POST.get("job_category")
        city = request.POST.get("city")

        experience = request.POST.get("experience")
        current_salary = request.POST.get("current_salary")
        expected_salary = request.POST.get("expected_salary")

        facebook_link = request.POST.get("facebook_link")
        linkedin_link = request.POST.get("linkedin_link")
        twitter_link = request.POST.get("twitter_link")
        github_link = request.POST.get("github_link")
        instagram_link = request.POST.get("instagram_link")
        discord_link = request.POST.get("discord_link")

        app_user.agency_name = agency_name
        app_user.agency_logo = agency_logo
        app_user.bio = bio
        app_user.charge = charge
        app_user.profile_photo = profile_photo
        app_user.user.first_name = first_name
        app_user.user.last_name = last_name
        app_user.user.save()
        
        app_user.age = age
        app_user.gender = gender
        app_user.phone_no = phone
        app_user.address = address
        app_user.country = country

        app_user.postcode = postcode
        app_user.language = language
        app_user.job_category = job_category
        app_user.city = city

        app_user.experience = experience
        app_user.current_salary = current_salary
        app_user.expected_salary = expected_salary

        app_user.facebook_link = facebook_link
        app_user.linkedin_link = linkedin_link
        app_user.twitter_link = twitter_link
        app_user.github_link = github_link
        app_user.instagram_link = instagram_link
        app_user.discord_link = discord_link

        app_user.save()

        messages.warning(request, "Welldone! Profiile Data Updated")
        return HttpResponseRedirect(reverse("resume:index"))





    else:
        recruits = AppUser.objects.filter(account_type="candidate").order_by('-pub_date')

        context = {"recruits": recruits, "app_user": app_user,}
        return render(request, "app_user/update_profile.html", context )




def AllRecruitView(request):
    app_user = AppUser.objects.get(user__pk=request.user.id)
    if request.method == "POST":
        pass


    else:
        recruits = AppUser.objects.filter(account_type="candidate").order_by('-pub_date')

        context = {"recruits": recruits, "app_user": app_user,}
        return render(request, "app_user/all_recruits.html", context )



def AppUserDetail2View(request, wallet_address):
    try:
        app_user = AppUser.objects.get(user__pk=request.user.id)
    except:
        app_user = None
        
    if request.method == "POST":
        pass


    else:
        recruit = AppUser.objects.get(wallet_address=wallet_address)

        context = {"app_user": app_user, "recruit": recruit}
        return render(request, "app_user/app_user_detail2.html", context )




@login_required(login_url='/app_user/sign_in/')
def AppUserDetailView(request, app_user_id):
    app_user = AppUser.objects.get(user__pk=request.user.id)
    if request.method == "POST":
        pass


    else:
        recruit = AppUser.objects.get(id=app_user_id)

        context = {"app_user": app_user, "recruit": recruit}
        return render(request, "app_user/app_user_detail.html", context )


def TempView(request):
    if request.method == "POST":
        pass


    else:
        context = {}
        return render(request, "app_user/app.html", context )



def ProfileView(request):
    if request.method == "POST":
        pass


    else:
        context = {}
        return render(request, "app_user/profile.html", context )


def MaintainView(request):
    if request.method == "POST":
        pass


    else:
        context = {}
        return render(request, "app_user/maintainance.html", context )
        
def ChangePasswordView(request):

    app_user = AppUser.objects.get(user__pk=request.user.id)
    if request.method == "POST":
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        
        user = app_user.user
        user.set_password(str(password2))
        user.save()
    
        messages.warning(request, "New Password Created!")
        return HttpResponseRedirect(reverse("app_user:sign_in"))


    else:
        pass

        context = {"app_user": app_user}
        
        return render(request, "app_user/change_password.html", context)

def error_404(request, exception):
    return render(request,'app_user/404.html')
    
def error_500(request):
    return render(request,'app_user/500.html')