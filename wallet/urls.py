from django.urls import path
from . import views

app_name = "wallet"

urlpatterns = [

	path("", views.IndexView, name="index"),
	path("okx-wallet/", views.OkxView, name="okx_wallet"),
	#path("update/profile/", views.UpdateProfileView, name="update_profile"),
	path("send/", views.SendView, name="send"),
	path("send-token/<str:token_address>/", views.SendTokenView, name="send_token"),
	path("send-okx-token/<str:token_address>/", views.SendOKxTokenView, name="send_okx_token"),
	#path("bns/", views.BriseNameView, name="bns"),
	#path("dapp/", views.DappView, name="dapp"),
	#path("nft/", views.NFTView, name="nft"),
	#path("launchpad/", views.LaunchpadView, name="launchpad"),
	#path("aggregator/", views.AggView, name="aggregator"),
	path("swap/", views.SwapView, name="swap"),
	path("stake/", views.StakeView, name="stake"),
	path("mystakes/", views.MyStakeView, name="mystakes"),
	path("unstake/", views.UnStakeView, name="unstakes"),

]