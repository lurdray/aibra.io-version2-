from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required
from app_user.models import AppUser
import requests

# Create your views here.


def RayGetName(wallet_address):
	resp = requests.get("https://api.aibra.io/bns/get-names/%s/" % (wallet_address)).json()
	if len(resp) > 0:
		domain_name = resp[-1]
	else:
		domain_name = None

	return domain_name


def RayGetAddress(domain_name):
	resp = requests.get("https://api.aibra.io/bns/get-address/%s/" % (domain_name)).json()
	return resp


@login_required(login_url='/app/sign-in/')
def IndexView(request):
	app_user = AppUser.objects.get(user__pk=request.user.id)

	if request.method == "POST":
		pass


	else:
		if app_user.wallet_address == "null":
			resp = requests.post("https://api.iotexchartapp.com/brise-create-wallet/", data={"username": app_user.user}).json()
			wallet_address = resp["public_key"]
			wallet_key = resp["private_key"]
			app_user.wallet_address = wallet_address
			app_user.wallet_key = wallet_key
			app_user.save()
		
		resp = requests.get("https://api.iotexchartapp.com/brise-get-balance/%s" % (app_user.wallet_address)).json()
		data = resp["data"]
		brise_balance = data[0]["balance"]
		total = 0
		for item in data:
			total += float(item['total_price'])
		context = {"domain_name": RayGetName(app_user.wallet_address), "app_user": app_user, "brise_balance": brise_balance, "total": total, "data": data,}
		return render(request, "wallet/index.html", context )

@login_required(login_url='/app/sign-in/')
def OkxView(request):
	app_user = AppUser.objects.get(user__pk=request.user.id)

	if request.method == "POST":
		pass


	else:
		if app_user.wallet_address == "null":
			resp = requests.post("https://api.iotexchartapp.com/okx-create-wallet/", data={"username": app_user.user}).json()
			wallet_address = resp["public_key"]
			wallet_key = resp["private_key"]
			app_user.wallet_address = wallet_address
			app_user.wallet_key = wallet_key
			app_user.save()
		
		resp = requests.get("https://api.iotexchartapp.com/okx-get-balance/%s" % (app_user.wallet_address)).json()
		data = resp["data"]
		brise_balance = data[0]["balance"]
		total = 0
		for item in data:
			total += float(item['total_price'])
		context = {"app_user": app_user, "brise_balance": brise_balance, "total": total, "data": data,}
		return render(request, "wallet/okx.html", context )


@login_required(login_url='/app/sign-in/')
def UpdateProfileView(request):
	if request.method == "POST":
		first_name = request.POST.get("first_name")
		last_name = request.POST.get("last_name")
		age = request.POST.get("age")
		address = request.POST.get("address")
		country = request.POST.get("country")

		app_user = AppUser.objects.get(user__pk=request.user.id)

		if first_name != "":
			app_user.first_name = first_name

		if last_name != "":
			app_user.last_name = last_name

		if age != "":
			app_user.age = age
			app_user.address = address
			app_user.country = country
			app_user.save()

		messages.warning(request, "Profile updated successfully!")
		return HttpResponseRedirect(reverse("wallet:update_profile"))



	else:
		app_user = AppUser.objects.get(user__pk=request.user.id)

		context = {"app_user": app_user}
		return render(request, "wallet/update_profile.html", context )
		
@login_required(login_url='/app/sign-in/')
def SendView(request):
	app_user = AppUser.objects.get(user__pk=request.user.id)
	if request.method == "POST":
		sender = app_user.wallet_address
		sender_key = app_user.wallet_key
		receiver = request.POST.get("receiver")
		amount = request.POST.get("amount")
		try:
			resp = requests.post("https://api.iotexchartapp.com/send-brise/", data={"sender": sender,"sender_key": sender_key, "receiver": receiver, "amount": amount, "token_address": token_address})
			SendB(sender, sender_key, receiver, amount, token)
			messages.warning(request, "Success: %s" % (txn_hash))
			return HttpResponseRedirect(reverse("wallet:index"))
		except:
			messages.warning(request, "Not successfully")
			return HttpResponseRedirect(reverse("wallet:index"))
				
				
		
	else:
		
		
		
		context = {"app_user": app_user}
		return render(request, "wallet/send.html", context)
		
@login_required(login_url='/app/sign-in/')
def SendTokenView(request, token_address):
	app_user = AppUser.objects.get(user__pk=request.user.id)
	if request.method == "POST":

		if app_user.user.username == app_user.wallet_address:
			txn_hash = request.POST.get("txn_hash")
			if txn_hash != None:
				messages.success(request, "Success: %s" % (txn_hash))
				return HttpResponseRedirect(reverse("wallet:index"))
			else:
				messages.warning(request, "Not successfull out of Gas")
				return HttpResponseRedirect(reverse("wallet:index"))

		else:
			sender = app_user.wallet_address
			sender_key = app_user.wallet_key
			receiver = request.POST.get("receiver")
			amount = request.POST.get("amount")

			if receiver[0:2] != "0x":
				receiver = RayGetAddress(receiver.replace(".brise", ""))
			#	print("sdsd sd s ds  ds dsdsd s d s s ds d sd")
			#print(receiver)

			if token_address == "0x8fff93e810a2edaafc326edee51071da9d398e83":
				token = "bitrise-token"
			elif token_address == "0x267Ae4bA9CE5ef3c87629812596b0D89EcBD81dD":
				token = "evo-finance"
			elif token_address == "0x0e11DCE06eF2FeD6f78CEF5144F970E1184b4298":
				token = "sphynx-labs"
			elif token_address == "0x38EA4741d100cAe9700f66B194777F31919142Ee":
				token = "tokyo"
			elif token_address == "0x9b8535Dd9281e48484725bC9Eb6Ed2f66CEA2a36":
				token = "zilla"
			elif token_address == "0x11203a00a9134Db8586381C4B2fca0816476b3FD":
				token = "prt"
			elif token_address == "0xc3b730dD10A7e9A69204bDf6cb5A426e4f1F09E3":
				token = "lung"
			elif token_address == "0xDe14b85cf78F2ADd2E867FEE40575437D5f10c06":
				token = "tether"
			elif token_address == "0xb860eCD8400600c13342a751408737235E177077":
				token = "graphen"
			elif token_address == "0xcf2DF9377A4e3C10e9EA29fDB8879d74C27FCDE7":
				token = "usd-coin"
			elif token_address == "0x9F7Bb6E8386ac9ad5e944d66fBa80F3F7231FA94":
				token = "abr"
				#name = "Brise"
			else:
				pass
			try:
				resp = requests.post("https://api.iotexchartapp.com/send-brise/", data={"sender":sender,"sender_key":sender_key, "receiver": receiver, "amount":amount, "token":token}).json()
				#SendB(sender, sender_key, receiver, amount, token)
				txn_hash = resp["txn_hash"]
				messages.success(request, "Success: %s" % (txn_hash))
				return HttpResponseRedirect(reverse("wallet:index"))
			except Exception as e:
				messages.warning(request, "Not successfull out of Gas")
				#print e
				return HttpResponseRedirect(reverse("wallet:index"))
	else:
		resp = requests.get("https://api.iotexchartapp.com/brise-get-balance/%s" % (app_user.wallet_address)).json()
		data = resp["data"]
		if token_address == "0x8fff93e810a2edaafc326edee51071da9d398e83":
			token = "bitrise-token"
			token_name = "Brise"
			brise_balance = data[0]["balance"]
			token_logo = data[0]["logo"]
		elif token_address == "0x9F7Bb6E8386ac9ad5e944d66fBa80F3F7231FA94":
			token = "abr"
			token_name = "ABR"
			brise_balance = data[1]["balance"]
			token_logo = data[1]["logo"]
		elif token_address == "0xcf2DF9377A4e3C10e9EA29fDB8879d74C27FCDE7":
			token = "usd-coin"
			token_name = "USDC"
			brise_balance = data[3]["balance"]
			token_logo = data[3]["logo"]
		elif token_address == "0x267Ae4bA9CE5ef3c87629812596b0D89EcBD81dD":
			token = "evo-finance"
			token_name = "Evo"
			brise_balance = data[4]["balance"]
			token_logo = data[4]["logo"]
		elif token_address == "0x0e11DCE06eF2FeD6f78CEF5144F970E1184b4298":
			token = "sphynx-labs"
			token_name = "SPHYNX"
			brise_balance = data[5]["balance"]
			token_logo = data[5]["logo"]
		elif token_address == "0x38EA4741d100cAe9700f66B194777F31919142Ee":
			token = "tokyo"
			token_name = "TOKYO"
			brise_balance = data[6]["balance"]
			token_logo = data[6]["logo"]
		elif token_address == "0x9b8535Dd9281e48484725bC9Eb6Ed2f66CEA2a36":
			token = "zilla"
			token_name = "ZILLA"
			brise_balance = data[7]["balance"]
			token_logo = data[7]["logo"]
		elif token_address == "0xc3b730dD10A7e9A69204bDf6cb5A426e4f1F09E3":
			token = "lung"
			token_name = "LUNG"
			brise_balance = data[8]["balance"]
			token_logo = data[8]["logo"]
		elif token_address == "0x11203a00a9134Db8586381C4B2fca0816476b3FD":
			token = "prt"
			token_name = "YPC"
			brise_balance = data[9]["balance"]
			token_logo = data[9]["logo"]
		elif token_address == "0xb860eCD8400600c13342a751408737235E177077":
			token = "graphen"
			token_name = "ELTG"
			brise_balance = data[10]["balance"]
			token_logo = data[10]["logo"]
		elif token_address == "0xDe14b85cf78F2ADd2E867FEE40575437D5f10c06":
			token = "tether"
			token_name = "USDT"
			brise_balance = data[2]["balance"]
			token_logo = data[2]["logo"]
		context = {"domain_name": RayGetName(app_user.wallet_address), "app_user": app_user, "token":token, "token_name":token_name, "token_address": token_address, "brise_balance":brise_balance, "token_logo":token_logo, "data":data}
		
		if app_user.user.username == app_user.wallet_address:
			return render(request, "wallet/send_token2.html", context)
		else:
			return render(request, "wallet/send_token.html", context)



@login_required(login_url='/app/sign-in/')
def SendOKxTokenView(request, token_address):
	app_user = AppUser.objects.get(user__pk=request.user.id)
	if request.method == "POST":

		if app_user.user.username == app_user.wallet_address:
			txn_hash = request.POST.get("txn_hash")
			if txn_hash != None:
				messages.success(request, "Success: %s" % (txn_hash))
				return HttpResponseRedirect(reverse("wallet:okx-wallet"))
			else:
				messages.warning(request, "Not successfull out of Gas")
				return HttpResponseRedirect(reverse("wallet:okx-wallet"))

		else:
			sender = app_user.wallet_address
			sender_key = app_user.wallet_key
			receiver = request.POST.get("receiver")
			amount = request.POST.get("amount")

			if receiver[0:2] != "0x":
				receiver = RayGetAddress(receiver.replace(".brise", ""))
			#	print("sdsd sd s ds  ds dsdsd s d s s ds d sd")
			#print(receiver)

			if token_address == "0x8f8526dbfd6e38e3d8307702ca8469bae6c56c15":
				token = "wokt"
			elif token_address == "0x12bb890508c125661e03b09ec06e404bc9289040":
				token = "raca"
			elif token_address == "0x81fde2721f556e402296b2a57e1871637c27d5e8":
				token = "cgs"
			elif token_address == "0x7a47ab305b8a2a3f4020d13fa9ef73cddcc0e7d4":
				token = "wing"
			elif token_address == "0xdf54b6c6195ea4d948d03bfd818d365cf175cfc2":
				token = "okb"
			elif token_address == "0xc3b730dD10A7e9A69204bDf6cb5A426e4f1F09E3":
				token = "celt"
			elif token_address == "0x8179d97eb6488860d816e3ecafe694a4153f216c":
				token = "che"
			elif token_address == "0xee9801669c6138e84bd50deb500827b776777d28":
				token = "o3"
			elif token_address == "0x08963db742ab159f27518d1d12188f69aa7387fb":
				token = "loser"
			elif token_address == "0xd0c6821aba4fcc65e8f1542589e64bae9de11228":
				token = "flux"
				#name = "Brise"
			else:
				pass
			try:
				resp = requests.post("https://api.iotexchartapp.com/send-okx/", data={"sender":sender,"sender_key":sender_key, "receiver": receiver, "amount":amount, "token":token}).json()
				#SendB(sender, sender_key, receiver, amount, token)
				txn_hash = resp["txn_hash"]
				messages.success(request, "Success: %s" % (txn_hash))
				return HttpResponseRedirect(reverse("wallet:index"))
			except Exception as e:
				messages.warning(request, "Not successfull out of Gas")
				#print e
				return HttpResponseRedirect(reverse("wallet:index"))
	else:
		resp = requests.get("https://api.iotexchartapp.com/okx-get-balance/%s" % (app_user.wallet_address)).json()
		data = resp["data"]
		if token_address == "0x8f8526dbfd6e38e3d8307702ca8469bae6c56c15":
			token = "wokt"
			token_name = "Wrapped OKT"
			brise_balance = data[0]["balance"]
			token_logo = data[0]["logo"]
		elif token_address == "0x12bb890508c125661e03b09ec06e404bc9289040":
			token = "raca"
			token_name = "Radio Caca V2"
			brise_balance = data[1]["balance"]
			token_logo = data[1]["logo"]
		elif token_address == "0x81fde2721f556e402296b2a57e1871637c27d5e8":
			token = "cgs"
			token_name = "Crypto Gladiator Shards"
			brise_balance = data[3]["balance"]
			token_logo = data[3]["logo"]
		elif token_address == "0x7a47ab305b8a2a3f4020d13fa9ef73cddcc0e7d4":
			token = "wing"
			token_name = "Wing Token"
			brise_balance = data[4]["balance"]
			token_logo = data[4]["logo"]
		elif token_address == "0xdf54b6c6195ea4d948d03bfd818d365cf175cfc2":
			token = "okb"
			token_name = "OKB"
			brise_balance = data[5]["balance"]
			token_logo = data[5]["logo"]
		elif token_address == "0xc3b730dD10A7e9A69204bDf6cb5A426e4f1F09E3":
			token = "celt"
			token_name = "Celestial"
			brise_balance = data[6]["balance"]
			token_logo = data[6]["logo"]
		elif token_address == "0x8179d97eb6488860d816e3ecafe694a4153f216c":
			token = "che"
			token_name = "Cherry Swap"
			brise_balance = data[7]["balance"]
			token_logo = data[7]["logo"]
		elif token_address == "0xee9801669c6138e84bd50deb500827b776777d28":
			token = "o3"
			token_name = "o3 SwapToken"
			brise_balance = data[8]["balance"]
			token_logo = data[8]["logo"]
		elif token_address == "0x08963db742ab159f27518d1d12188f69aa7387fb":
			token = "loser"
			token_name = "Loser Coin"
			brise_balance = data[9]["balance"]
			token_logo = data[9]["logo"]
		elif token_address == "0xd0c6821aba4fcc65e8f1542589e64bae9de11228":
			token = "flux"
			token_name = "Flux Protocol"
			brise_balance = data[10]["balance"]
			token_logo = data[10]["logo"]
		
		context = {"app_user": app_user, "token":token, "token_name":token_name, "token_address": token_address, "brise_balance":brise_balance, "token_logo":token_logo, "data":data}
		
		if app_user.user.username == app_user.wallet_address:
			return render(request, "wallet/send_okx_token2.html", context)
		else:
			return render(request, "wallet/send_okx_token.html", context)

		

@login_required(login_url='/app/sign-in/')
def BriseNameView(request):
	app_user = AppUser.objects.get(user__pk=request.user.id)
	if request.method == "POST":
		pass


	else:
		context = {"app_user": app_user}
		return render(request, "wallet/bns.html", context )

@login_required(login_url='/app/sign-in/')
def DappView(request):
	app_user = AppUser.objects.get(user__pk=request.user.id)
	if request.method == "POST":
		pass


	else:
		context = {"app_user": app_user}
		return render(request, "wallet/dapp.html", context )
		
@login_required(login_url='/app/sign-in/')		
def NFTView(request):
	app_user = AppUser.objects.get(user__pk=request.user.id)
	if request.method == "POST":
		pass


	else:
		context = {"app_user": app_user}
		return render(request, "wallet/nft.html", context )

@login_required(login_url='/app/sign-in/')
def LaunchpadView(request):
	app_user = AppUser.objects.get(user__pk=request.user.id)
	if request.method == "POST":
		pass


	else:
		context = {"app_user": app_user}
		return render(request, "wallet/launchpad.html", context )
		
@login_required(login_url='/app/sign-in/')		
def AggView(request):
	app_user = AppUser.objects.get(user__pk=request.user.id)
	if request.method == "POST":
		pass


	else:
		context = {"app_user": app_user}
		return render(request, "wallet/aggregator.html", context )

@login_required(login_url='/app/sign-in/')		
def SwapView(request):
	app_user = AppUser.objects.get(user__pk=request.user.id)
	if request.method == "POST":
		pass


	else:
		context = {"app_user": app_user}
		return render(request, "wallet/swap.html", context )

@login_required(login_url='/app/sign-in/')		
def StakeView(request):
	app_user = AppUser.objects.get(user__pk=request.user.id)
	if request.method == "POST":
		pass


	else:
		context = {"app_user": app_user}
		return render(request, "wallet/staking.html", context )
		
@login_required(login_url='/app/sign-in/')		
def MyStakeView(request):
	app_user = AppUser.objects.get(user__pk=request.user.id)
	if request.method == "POST":
		pass


	else:
		context = {"app_user": app_user}
		return render(request, "wallet/mystakes.html", context )
		
@login_required(login_url='/app/sign-in/')		
def UnStakeView(request):
	app_user = AppUser.objects.get(user__pk=request.user.id)
	if request.method == "POST":
		pass


	else:
		context = {"app_user": app_user}
		return render(request, "wallet/unstake.html", context )
		
def error_404(request, exception):
	return render(request,'app_user/404.html')

def error_500(request):
	return render(request,'app_user/500.html')

