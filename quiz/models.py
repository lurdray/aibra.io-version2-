from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from app_user.models import AppUser

# Create your models here.



class Result(models.Model):
	app_user = models.ForeignKey(AppUser, on_delete=models.CASCADE)

	score = models.IntegerField(default=0)
	total = models.IntegerField(default=0)
	percentage = models.IntegerField(default=50)

	pub_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.percentage




class QandA(models.Model):
	title = models.TextField()
	answer_a = models.CharField(max_length=50, default="None")
	answer_b = models.CharField(max_length=50, default="None")
	answer_c = models.CharField(max_length=50, default="None")
	answer_d = models.CharField(max_length=50, default="None")
	answer = models.CharField(max_length=50, default="None")

	category = models.CharField(max_length=50, default="general")
	level = models.CharField(max_length=50, default="simple")

	
	pub_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.title




class Quiz(models.Model):
	title = models.CharField(max_length=50, default="none")
	detail = models.TextField(default="none")
	duration = models.CharField(max_length=50, default="none")

	question_no = models.IntegerField(default=1)
	barrier = models.IntegerField(default=50)

	start = models.DateTimeField(default=timezone.now)
	end = models.DateTimeField(default=timezone.now)

	QandAs = models.ManyToManyField(QandA, through="QuizQandAConnector")

	link = models.CharField(max_length=50, default="none")

	status = models.BooleanField(default=False)
	pub_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.title




class QuizQandAConnector(models.Model):
	quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
	qanda = models.ForeignKey(QandA, on_delete=models.CASCADE)
	pub_date = models.DateTimeField(default=timezone.now)
