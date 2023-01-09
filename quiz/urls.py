from django.urls import path
from . import views

app_name = "quiz"

urlpatterns = [

	path("setup-quiz/", views.SetupQuizView, name="setup_quiz"),
	path("add-qa/<int:quiz_id>/", views.AddQAView, name="add_qa"),

	path("take-quiz/<int:job_id>/", views.TakeQuizView, name="take_quiz"),
	path("complete-quiz/<int:result_id>/", views.CompleteQuizView, name="complete_quiz"),

	path("see-result/<int:app_user_id>/", views.SeeResultView, name="see_result"),

]