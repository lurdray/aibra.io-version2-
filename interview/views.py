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

#from .forms import UserForm





def IndexView(request):
	if request.method == "POST":
		pass


	else:
		context = {}
		return render(request, "interview/index.html", context )





def SetupInterviewView(request, job_id):
	if request.method == "POST":
		pass


	else:
		context = {}
		return render(request, "interview/setup_interview.html", context )

def error_404(request, exception):
	return render(request,'app_user/404.html')
	
def error_500(request):
	return render(request,'app_user/500.html')