from django.contrib import messages
from django.shortcuts import (HttpResponse, HttpResponseRedirect,
                              get_object_or_404, redirect, render)
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User

from app_user.models import AppUser
from stake.models import Stake
import datetime

import requests


def IndexView(request):
    app_user = AppUser.objects.get(user__pk=request.user.id)
    if app_user.user.username == "odiagaraymondrayray@gmail.com":
        if request.method == "POST":
            pass

            
        else:
            stakes = Stake.objects.filter(closed_status=False).order_by('-pub_date')
            stakes_done = Stake.objects.filter(closed_status=True).order_by('-pub_date')
            stakes_request = Stake.objects.filter(request_payment_status=True).order_by('-pub_date')
            
            context = {"stakes": stakes, "stakes_done": stakes_done, "stakes_request": stakes_request}
            return render(request, "admin_app/index.html", context)

    else:
        return HttpResponse(str("Error, please contact Admins!"))



def StakingDetailView(request, staking_id):
    app_user = AppUser.objects.get(user__pk=request.user.id)
    if app_user.user.username == "odiagaraymondrayray@gmail.com":
        if request.method == "POST":
            stake = Stake.objects.get(id=staking_id)
            
            sender = app_user.wallet_address
            sender_key = app_user.wallet_key
            receiver = request.POST.get("wallet_address")
            amount = request.POST.get("amount")
            token = "abr"
        
            try:
                resp = requests.post("https://api.iotexchartapp.com/send-brise/", data={"sender":sender,"sender_key":sender_key, "receiver": receiver, "amount":amount, "token":token}).json()
                txn_hash = resp["txn_hash"]
                
            except Exception as e:
                txn_hash = None

            if txn_hash:
                stake.closed_status = True
                stake.save()
            
                messages.warning(request, "Congratulations! You have approved a payment. %s" % (txn_hash))
                
                return HttpResponseRedirect(reverse("admin_app:index"))

            else:
                #return HttpResponse(str(txn_hash))
                messages.warning(request, "Sorry! Approval did not go through successfully.")
                return HttpResponseRedirect(reverse("admin_app:staking_detail", args=[staking_id]))

            
        else:
            today_date = datetime.date.today()
            stake = Stake.objects.get(id=staking_id)

            context = {"stake": stake, "today_date": today_date}
            return render(request, "admin_app/staking_detail.html", context)

    else:
        return HttpResponse(str("Error, please contact Admins!"))