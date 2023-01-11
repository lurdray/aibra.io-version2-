
from django.contrib import messages
from django.shortcuts import (HttpResponse, HttpResponseRedirect,
                            get_object_or_404, redirect, render)
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User

from app_user.models import *
from stake.models import *
import requests

from django.utils import timezone
import datetime
from django.contrib.auth.decorators import login_required

from wallet.views import RayGetName

@login_required(login_url='/app/sign-up/')
def IndexView(request):
    app_user = AppUser.objects.get(user__pk=request.user.id)

    if app_user.user.username == app_user.wallet_address:
        return HttpResponseRedirect(reverse("staking:stake_metamask2"))
    else:
        return HttpResponseRedirect(reverse("staking:stake"))



@login_required(login_url='/app/sign-up/')
def StakeView(request):
    app_user = AppUser.objects.get(user__pk=request.user.id)
    if request.method == "POST":
        amount = float(request.POST.get("amount"))
        app_user = AppUser.objects.get(user__pk=request.user.id)
        duration = request.POST.get("duration")

        bep_balance = requests.get("https://api.iotexchartapp.com/aibra/get-balance/%s/" % (app_user.wallet_address)).json()

        #return HttpResponse(str(float(bep_balance["data"][0]["balance"])))
        if float(float(bep_balance["data"][0]["balance"])) > amount:
            
            sender = app_user.wallet_address
            sender_key = app_user.wallet_key
            receiver = "0xbCA60DDe596B82a4Cb8CC3233BF8f0ED09280557"
            amount = amount
            token = "abr"
        
            try:
                resp = requests.post("https://api.iotexchartapp.com/send-brise/", data={"sender":sender,"sender_key":sender_key, "receiver": receiver, "amount":amount, "token":token}).json()
                txn_hash = resp["txn_hash"]
                
            except:
                txn_hash = None
                
            sender = app_user.wallet_address
            sender_key = app_user.wallet_key
            receiver = "0xbCA60DDe596B82a4Cb8CC3233BF8f0ED09280557"
            amount2 = float(amount*0.01)
            token = "abr"
        
            #try:
            #    resp2 = requests.post("https://api.iotexchartapp.com/send-brise/", data={"sender":sender,"sender_key":sender_key, "receiver": receiver, "amount":amount2, "token":token}).json()
            #    txn_hash2 = resp2["txn_hash"]
                
            #except:
            #    txn_hash2 = None
                

            #return HttpResponse(str(txn_hash))
            if txn_hash != None:
                stake = Stake.objects.create(app_user=app_user, amount=amount, duration=duration)
                stake.save()

                #returns block
                if duration == "60":
                    returns = float(amount) + float(amount)*0.1 #25%
                    returnsk = float(float(returns)*0.03) + float(float(amount)*0.01)
                    returns = float(returns) - float(returnsk)
            
                else:
                    returns = float(amount) + float(amount)*0.1 #25%
                stake.returns = returns

                payment_hash = txn_hash
                stake.payment_hash = payment_hash
                stake.payment_status = True
                stake.amount_tax = float(float(amount)*0.01)
                stake.returns_tax = float(float(returns)*0.03)
                stake.total_tax = returnsk
                stake.payment_confirmation_status = True
                

                today = timezone.now().date()
                due_date = today + datetime.timedelta(days=int(duration))
                stake.due_date = due_date

                stake.save()

                messages.warning(request, "Congratulations! you have successfully staked your asset! %s" % (txn_hash))
                return HttpResponseRedirect(reverse("staking:my_stakes"))

            else:
                messages.warning(request, "Sorry!! your staking could not go through.(Try top-up your account.._")
                return HttpResponseRedirect(reverse("staking:stake"))

        else:
                messages.warning(request, "Sorry! something went wrong. (Try top-up your account.)")
                return HttpResponseRedirect(reverse("staking:stake"))


    else:
        #resp = requests.get("https://api.iotexchartapp.com/brise-get-balance/%s" % (app_user.wallet_address)).json()
        #data = resp["data"]
        bep_balance = requests.get("https://api.iotexchartapp.com/aibra/get-balance/%s/" % (app_user.wallet_address)).json()
        brise_balance = float(float(bep_balance["data"][0]["balance"]))
        context = {"domain_name": RayGetName(app_user.wallet_address), "app_user": app_user, "brise_balance":brise_balance}
        return render(request, "stake/staking.html", context)


@login_required(login_url='/app/sign-up/')
def StakeWithMView(request):
    app_user = AppUser.objects.get(user__pk=request.user.id)
    if request.method == "POST":
        amount = float(request.POST.get("amount"))
        app_user = AppUser.objects.get(user__pk=request.user.id)
        duration = request.POST.get("duration")

        bep_balance = requests.get("https://api.iotexchartapp.com/aibra/get-balance/%s/" % (app_user.wallet_address)).json()

        #return HttpResponse(str(float(bep_balance["data"][0]["balance"])))
        if float(float(bep_balance["data"][0]["balance"])) > amount:
            
            sender = app_user.wallet_address
            txn_hash = None
            if txn_hash != None:
                stake = Stake.objects.create(app_user=app_user, amount=amount, duration=duration)
                stake.save()

                #returns block
                if duration == "60":
                    returns = float(amount) + float(amount)*0.1 #25%
                    returnsk = float(float(returns)*0.03) + float(float(amount)*0.01)
                    returns = float(returns) - float(returnsk)
            
                else:
                    returns = float(amount) + float(amount)*0.1 #25%
                stake.returns = returns

                payment_hash = txn_hash
                stake.payment_hash = payment_hash
                stake.payment_status = True
                stake.amount_tax = float(float(amount)*0.01)
                stake.returns_tax = float(float(returns)*0.03)
                stake.total_tax = returnsk
                stake.payment_confirmation_status = True
                

                today = timezone.now().date()
                due_date = today + datetime.timedelta(days=int(duration))
                stake.due_date = due_date

                stake.save()

                messages.warning(request, "Congratulations! you have successfully staked your asset! %s" % (txn_hash))
                return HttpResponseRedirect(reverse("staking:my_stakes"))

            else:
                messages.warning(request, "Sorry!! your staking could not go through.(Try top-up your account.._")
                return HttpResponseRedirect(reverse("staking:stake_metamask2"))

        else:
                messages.warning(request, "Sorry! something went wrong. (Try top-up your account.)")
                return HttpResponseRedirect(reverse("staking:stake_metamask2"))


    else:
        #resp = requests.get("https://api.iotexchartapp.com/brise-get-balance/%s" % (app_user.wallet_address)).json()
        #data = resp["data"]
        bep_balance = requests.get("https://api.iotexchartapp.com/aibra/get-balance/%s/" % (app_user.wallet_address)).json()
        brise_balance = float(float(bep_balance["data"][0]["balance"]))
        context = {"app_user": app_user, "brise_balance":brise_balance}
        return render(request, "stake/staking2.html", context)
    
@login_required(login_url='/app/sign-up/')
def StakeWithM2View(request):
    app_user = AppUser.objects.get(user__pk=request.user.id)
    if request.method == "POST":
        amount = float(request.POST.get("amount"))
        txn_hash = request.POST.get("txn_hash")
        duration = "60"

        if txn_hash != "none": #it worked
            
            stake = Stake.objects.create(app_user=app_user, amount=amount, duration=duration)
            stake.save()

            #returns block
            if duration == "60":
                returns = float(amount) + float(amount)*0.1 #25%
                returnsk = float(float(returns)*0.03) + float(float(amount)*0.01)
                returns = float(returns) - float(returnsk)
        
            else:
                returns = float(amount) + float(amount)*0.1 #25%
            stake.returns = returns

            payment_hash = txn_hash
            stake.payment_hash = payment_hash
            stake.payment_status = True
            stake.amount_tax = float(float(amount)*0.01)
            stake.returns_tax = float(float(returns)*0.03)
            stake.total_tax = returnsk
            stake.payment_confirmation_status = True
            

            today = timezone.now().date()
            due_date = today + datetime.timedelta(days=int(duration))
            stake.due_date = due_date

            stake.save()

            messages.warning(request, "Congratulations! you have successfully staked your asset! %s" % (txn_hash))
            return HttpResponseRedirect(reverse("staking:my_stakes"))

        else:
            messages.warning(request, "Sorry! The transaction did not go through.")
            return HttpResponseRedirect(reverse("staking:stake_metamask2"))



    else:
        #resp = requests.get("https://api.iotexchartapp.com/brise-get-balance/%s" % (app_user.wallet_address)).json()
        #data = resp["data"]
        bep_balance = requests.get("https://api.iotexchartapp.com/aibra/get-balance/%s/" % (app_user.wallet_address)).json()
        brise_balance = float(float(bep_balance["data"][0]["balance"]))
        context = {"domain_name": RayGetName(app_user.wallet_address), "app_user": app_user, "brise_balance":brise_balance}
        return render(request, "stake/staking3.html", context)

@login_required(login_url='/app/sign-up/')
def MakePaymentView(request, staking_id):
    app_user = AppUser.objects.get(user__pk=request.user.id)
    if request.method == "POST":

        stake = Stake.objects.get(id=staking_id)
        
        messages.warning(request, "Congratulations! You have made payment.")
        return HttpResponseRedirect(reverse("staking:confirm_payment", args=[stake.id,]))



    else:

        context = {}
        return render(request, "stake/make_payment.html", context)



@login_required(login_url='/app/sign-up/')
def ConfirmPaymentView(request, staking_id):
    app_user = AppUser.objects.get(user__pk=request.user.id)
    if request.method == "POST":
        stake = Stake.objects.get(id=staking_id)

        messages.warning(request, "Congratulations! You have confirm your payment.")
        return HttpResponseRedirect(reverse("staking:my_stakes"))

    else:

        context = {}
        return render(request, "stake/confirm_payment.html", context)


@login_required(login_url='/app/sign-up/')
def MyStakesView(request):
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

        my_stakes = Stake.objects.filter(app_user=app_user).order_by('-pub_date')
        
        from datetime import datetime
        if len(my_stakes) > 0:
            stake = my_stakes.last()
            last_date = datetime(int(str(stake.due_date)[:4]), int(str(stake.due_date)[5:7]), int(str(stake.due_date)[8:10]))
            launch_date = datetime(2022, 8, 16)
            if last_date > launch_date or last_date == launch_date:
                return_checker = "10%"
            else:
                return_checker = "25%"
            #return HttpResponse(str(launch_date))
        else:
            return_checker = None
            
        

        context = {"my_stakes": my_stakes, "app_user": app_user, "wallet_address": app_user.wallet_address, "1_per": 0.01, "3_per": 0.03, "return_checker":return_checker}
        return render(request, "stake/mystakes.html", context)



@login_required(login_url='/app/sign-up/')
def RequestPaymentView(request, staking_id):
    app_user = AppUser.objects.get(user__pk=request.user.id)
    if request.method == "POST":
        stake = Stake.objects.get(id=staking_id)

        from datetime import datetime
        due_date = datetime(int(str(stake.due_date)[:4]), int(str(stake.due_date)[5:7]), int(str(stake.due_date)[8:10]))
        today_date = datetime.now()

        if today_date > due_date or today_date == due_date:
            stake.request_payment_status = True
            stake.save()

            messages.warning(request, "Congratulations! Your request was successfull.")
            return HttpResponseRedirect(reverse("staking:my_stakes"))

        else:
            messages.warning(request, "Sorry! you can not request for payment at this time.")
            return HttpResponseRedirect(reverse("staking:my_stakes"))

    else:

        try:
            stake = Stake.objects.get(id=staking_id)
        except:
            stake = None
            
        from datetime import datetime
        due_date = datetime(int(str(stake.due_date)[:4]), int(str(stake.due_date)[5:7]), int(str(stake.due_date)[8:10]))
        today_date = datetime.now()

        if today_date > due_date or today_date == due_date:
            ready = True
        else:
            ready = False
            
        from datetime import datetime
        last_date = datetime(int(str(stake.due_date)[:4]), int(str(stake.due_date)[5:7]), int(str(stake.due_date)[8:10]))
        launch_date = datetime(2022, 8, 16)
        if last_date > launch_date or last_date == launch_date:
            return_checker = "10%"
        else:
            return_checker = "25%"


        context = {"stake": stake, "ready": ready, "return_checker": return_checker, "app_user":app_user}
        return render(request, "stake/request_payment.html", context)
        
def error_404(request, exception):
	return render(request,'app_user/404.html')        
        
def error_500(request):
	return render(request,'app_user/500.html')