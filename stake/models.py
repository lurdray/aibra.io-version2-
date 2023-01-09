from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from app_user.models import AppUser


class Stake(models.Model):
	app_user = models.ForeignKey(AppUser, on_delete=models.CASCADE)

	amount = models.FloatField(default=0)
	duration = models.IntegerField(default=0)
	returns = models.FloatField(default=0)
	
	amount_tax = models.FloatField(default=0)
	returns_tax = models.FloatField(default=0)
	total_tax = models.FloatField(default=0)
	
	payment_hash = models.CharField(default="none", max_length=50)
	payment_status = models.BooleanField(default=False)
	payment_confirmation_status = models.BooleanField(default=False)

	request_payment_status = models.BooleanField(default=False)
	closed_status = models.BooleanField(default=False)

	due_date = models.DateTimeField(default=timezone.now)
	pub_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.app_user.user.username

		