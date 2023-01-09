from django.urls import path
from . import views

app_name = "admin_app"

urlpatterns = [

	path("", views.IndexView, name="index"),
	path("staking-detail/<int:staking_id>/", views.StakingDetailView, name="staking_detail"),

]

