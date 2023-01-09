from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User

from django.core.mail import send_mail

from datetime import datetime
import datetime as dt
import requests

from quiz.models import *
from job.models import *

#from .forms import UserForm


def SetupQuizView(request):
	app_user = AppUser.objects.get(user__pk=request.user.id)

	if request.method == "POST":
		job_id = request.POST.get("job_id")
		job = Job.objects.get(id=job_id)

		title = request.POST.get("title")
		detail = request.POST.get("detail")
		duration = request.POST.get("duration")

		question_no = request.POST.get("question_no")
		barrier = request.POST.get("barrier")

		quiz = Quiz.objects.create(title=title, detail=detail, duration=duration,
			question_no=question_no, barrier=barrier)
		quiz.save()

		job.quiz = quiz
		job.save()

		return HttpResponseRedirect(reverse("quiz:add_qa", args=[quiz.id,]))


	else:
		my_jobs = Job.objects.filter(app_user=app_user)

		if my_jobs.count() == 0:
			messages.warning(request, "Add a job first")
			return HttpResponseRedirect(reverse("job:add_job"))

		else:
			context = {"app_user": app_user, "my_jobs": my_jobs}
			return render(request, "quiz/setup_quiz.html", context )


def AddQAView(request, quiz_id):
	app_user = AppUser.objects.get(user__pk=request.user.id)
	quiz = Quiz.objects.get(id=quiz_id)
	if request.method == "POST":
		q1 = request.POST.get("q1")
		category = request.POST.get("category")
		level = request.POST.get("level")

		q1 = request.POST.get("q1")
		q2 = request.POST.get("q2")
		q3 = request.POST.get("q3")
		q4 = request.POST.get("q4")
		q5 = request.POST.get("q5")
		q6 = request.POST.get("q6")
		q7 = request.POST.get("q7")
		q8 = request.POST.get("q8")
		q9 = request.POST.get("q9")
		q10 = request.POST.get("q10")

		if q1 != None:
			q1_a = request.POST.get("q1_a")
			q1_b = request.POST.get("q1_b")
			q1_c = request.POST.get("q1_c")
			q1_d = request.POST.get("q1_d")
			answer_1 = request.POST.get("answer_1")

			question1 = QandA.objects.create(title=q1, answer_a=q1_a,
				answer_b=q1_b, answer_c=q1_c, answer_d=q1_d, answer=answer_1)
			question1.save()

			qq = QuizQandAConnector(quiz=quiz, qanda=question1)
			qq.save()


		if q2 != None:
			q2_a = request.POST.get("q2_a")
			q2_b = request.POST.get("q2_b")
			q2_c = request.POST.get("q2_c")
			q2_d = request.POST.get("q2_d")
			answer_2 = request.POST.get("answer_2")

			question2 = QandA.objects.create(title=q2, answer_a=q2_a,
				answer_b=q2_b, answer_c=q2_c, answer_d=q2_d, answer=answer_2)
			question2.save()

			qq = QuizQandAConnector(quiz=quiz, qanda=question2)
			qq.save()
			
		
		if q3 != None:
			q3_a = request.POST.get("q3_a")
			q3_b = request.POST.get("q3_b")
			q3_c = request.POST.get("q3_c")
			q3_d = request.POST.get("q3_d")
			answer_3 = request.POST.get("answer_3")

			question3 = QandA.objects.create(title=q3, answer_a=q3_a,
				answer_b=q3_b, answer_c=q3_c, answer_d=q3_d, answer=answer_3)
			question3.save()

			qq = QuizQandAConnector(quiz=quiz, qanda=question3)
			qq.save()
			
			
		if q4 != None:
			q4_a = request.POST.get("q4_a")
			q4_b = request.POST.get("q4_b")
			q4_c = request.POST.get("q4_c")
			q4_d = request.POST.get("q4_d")
			answer_4 = request.POST.get("answer_4")

			question4 = QandA.objects.create(title=q4, answer_a=q4_a,
				answer_b=q4_b, answer_c=q4_c, answer_d=q4_d, answer=answer_4)
			question4.save()

			qq = QuizQandAConnector(quiz=quiz, qanda=question4)
			qq.save()
			
		if q5 != None:
			q5_a = request.POST.get("q5_a")
			q5_b = request.POST.get("q5_b")
			q5_c = request.POST.get("q5_c")
			q5_d = request.POST.get("q5_d")
			answer_5 = request.POST.get("answer_5")

			question5 = QandA.objects.create(title=q5, answer_a=q5_a,
				answer_b=q5_b, answer_c=q5_c, answer_d=q5_d, answer=answer_5)
			question5.save()

			qq = QuizQandAConnector(quiz=quiz, qanda=question5)
			qq.save()
			
		if q6 != None:
			q6_a = request.POST.get("q6_a")
			q6_b = request.POST.get("q6_b")
			q6_c = request.POST.get("q6_c")
			q6_d = request.POST.get("q6_d")
			answer_6 = request.POST.get("answer_6")

			question6 = QandA.objects.create(title=q6, answer_a=q6_a,
				answer_b=q6_b, answer_c=q6_c, answer_d=q6_d, answer=answer_6)
			question6.save()

			qq = QuizQandAConnector(quiz=quiz, qanda=question6)
			qq.save()
			
		if q7 != None:
			q7_a = request.POST.get("q7_a")
			q7_b = request.POST.get("q7_b")
			q7_c = request.POST.get("q7_c")
			q7_d = request.POST.get("q7_d")
			answer_7 = request.POST.get("answer_7")

			question7 = QandA.objects.create(title=q7, answer_a=q7_a,
				answer_b=q7_b, answer_c=q7_c, answer_d=q7_d, answer=answer_7)
			question7.save()

			qq = QuizQandAConnector(quiz=quiz, qanda=question7)
			qq.save()
			
		if q8 != None:
			q8_a = request.POST.get("q8_a")
			q8_b = request.POST.get("q8_b")
			q8_c = request.POST.get("q8_c")
			q8_d = request.POST.get("q8_d")
			answer_8 = request.POST.get("answer_8")

			question8 = QandA.objects.create(title=q8, answer_a=q8_a,
				answer_b=q8_b, answer_c=q8_c, answer_d=q8_d, answer=answer_8)
			question8.save()

			qq = QuizQandAConnector(quiz=quiz, qanda=question8)
			qq.save()
			
		if q9 != None:
			q9_a = request.POST.get("q9_a")
			q9_b = request.POST.get("q9_b")
			q9_c = request.POST.get("q9_c")
			q9_d = request.POST.get("q9_d")
			answer_9 = request.POST.get("answer_9")

			question9 = QandA.objects.create(title=q9, answer_a=q9_a,
				answer_b=q9_b, answer_c=q9_c, answer_d=q9_d, answer=answer_9)
			question9.save()

			qq = QuizQandAConnector(quiz=quiz, qanda=question9)
			qq.save()
			
		if q10 != None:
			q10_a = request.POST.get("q10_a")
			q10_b = request.POST.get("q10_b")
			q10_c = request.POST.get("q10_c")
			q10_d = request.POST.get("q10_d")
			answer_10 = request.POST.get("answer_10")

			question10 = QandA.objects.create(title=q10, answer_a=q10_a,
				answer_b=q10_b, answer_c=q10_c, answer_d=q10_d, answer=answer_10)
			question10.save()

			qq = QuizQandAConnector(quiz=quiz, qanda=question10)
			qq.save()


		else:
			pass



		messages.warning(request, "Questions Successfully Added")
		return HttpResponseRedirect(reverse("job:add_job"))

		


	else:
		context = {"app_user": app_user, "quiz": quiz}
		return render(request, "quiz/add_qa.html", context )



def TakeQuizView(request, job_id):
	app_user = AppUser.objects.get(user__pk=request.user.id)

	job = Job.objects.get(id=job_id)
	quiz = job.quiz

	questions = job.quiz.QandAs.all()
	if questions.count() > 0:

		counts = questions.count()
		count_list = []


		for i in range(counts):
			count_list.append(i+1)

		quiz_questions = zip(questions, count_list)

		if request.method == "POST":
			score = 0
			percentage = 0
			actual_score = 0
			real_score = 0

			answers = []
			answer_list = []
			for item, count in quiz_questions:
				val = "selected_answer_" + str(count)
				if request.POST.get(val):
					answers.append(request.POST.get(val))
				else:
					answers.append("x_x")

			for item in answers:
				answer_list.append(item.split("_")[1])


			for item, item2 in zip(questions, answer_list):
				if item.answer == item2:
					actual_score += 1

			percentage = (actual_score/counts)*100

			result = Result.objects.create(app_user=app_user, score=actual_score, total=count, percentage=percentage)
			result.save()

			jr = JobResultConnector(job=job, result=result)
			jr.save()

			return HttpResponseRedirect(reverse("quiz:complete_quiz", args=(result.id,)))


		else:

			context = {"app_user": app_user, "quiz": quiz, "quiz_questions": quiz_questions, "counts": counts}#, "time_exam_link": time_exam_link, "time_student_id": time_student_id}#, "time_result_id": time_result_id}
			return render(request, "quiz/take_quiz.html", context)

	else:
		return HttpResponseRedirect(reverse("job:index"))



def CompleteQuizView(request, result_id):
	app_user = AppUser.objects.get(user__pk=request.user.id)
	result = Result.objects.get(id=result_id)
	if request.method == "POST":
		pass


	else:

		context = {"result": result, "app_user": app_user}
		return render(request, "quiz/complete_quiz.html", context )



def SeeResultView(request, app_user_id):
	app_user = AppUser.objects.get(user__pk=request.user.id)
	result = Result.objects.filter(app_user__id=app_user_id).last()
	if request.method == "POST":
		pass


	else:

		context = {"result": result, "app_user": app_user, "app_user_id":app_user_id}
		return render(request, "quiz/see_result.html", context )

def error_404(request, exception):
	return render(request,'app_user/404.html')

def error_500(request):
	return render(request,'app_user/500.html')

























