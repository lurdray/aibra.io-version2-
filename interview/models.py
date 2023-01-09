from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.



class Interview(models.Model):
	title = models.CharField(max_length=50, default="none")
	detail = models.TextField(default="none")

	start = models.DateTimeField()
	end = models.DateTimeField()

	link = models.CharField(max_length=50, default="none")

	status = models.BooleanField(default=False)
	pub_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.title
