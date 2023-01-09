from django.urls import path
from . import views

app_name = "resume"

urlpatterns = [

	path("", views.IndexView, name="index"),
	path("update/resume/1/", views.UpdateResume1View, name="update_resume1"),

	path("update/resume/2/", views.UpdateResume2View, name="update_resume2"),


	path("update/resume/3/", views.UpdateResume3View, name="update_resume3"),
	path("update/resume/3/add-career/", views.AddCareerView, name="add_career"),
	path("update/resume/3/add-education/", views.AddEducationView, name="add_education"),
	path("update/resume/3/add-skill/", views.AddSkillView, name="add_skill"),

	path("update/resume/4/", views.UpdateResume4View, name="update_resume4"),
	path("update/resume/4/add-project/", views.AddProjectView, name="add_project"),
	path("update/resume/4/add-hobby/", views.AddHobbyView, name="add_hobby"),

	path("update/resume/5/", views.UpdateResume5View, name="update_resume5"),
	path("update/resume/5/add-award/", views.AddAwardView, name="add_award"),
	path("update/resume/5/add-referee/", views.AddRefereeView, name="add_referee"),


	#edits
	path("update/resume/5/edit-referee/<int:referee_id>/", views.EditRefereeView, name="edit_referee"),
	path("update/resume/5/edit-award/<int:award_id>/", views.EditAwardView, name="edit_award"),

	path("update/resume/5/edit-hobby/<int:hobby_id>/", views.EditHobbyView, name="edit_hobby"),
	path("update/resume/4/edit-project/<int:project_id>/", views.EditProjectView, name="edit_project"),
	path("update/resume/3/edit-skill/<int:skill_id>/", views.EditSkillView, name="edit_skill"),

	path("update/resume/3/edit-education/<int:education_id>/", views.EditEducationView, name="edit_education"),
	path("update/resume/3/edit-career/<int:career_id>/", views.EditCareerView, name="edit_career"),

	path("update/resume/2/edit-work-experience/<int:work_experience_id>/", views.EditResume2View, name="edit_resume2"),

]