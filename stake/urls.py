

from django.urls import path
from . import views

app_name = "staking"

urlpatterns = [

	path("", views.IndexView, name="index"),
	path("stake/", views.StakeView, name="stake"),
	path("stake/metamask/", views.StakeWithMView, name="stake_metamask"),
	path("stake/metamask/pay/", views.StakeWithM2View, name="stake_metamask2"),
	path("my-stakes/", views.MyStakesView, name="my_stakes"),

	path("make-payment/<int:staking_id>/", views.MakePaymentView, name="make_payment"),
	path("confirm-payment/<int:staking_id>/", views.ConfirmPaymentView, name="confirm_payment"),

	path("request-payment/<int:staking_id>/", views.RequestPaymentView, name="request_payment"),

]


