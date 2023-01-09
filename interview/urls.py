from django.urls import path
from . import views

app_name = "interview"

urlpatterns = [

	path("", views.IndexView, name="index"),
	path("setup-interview/<int:job_id>/", views.SetupInterviewView, name="setup_interview"),

	
]