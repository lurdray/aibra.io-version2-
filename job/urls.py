from django.urls import path
from . import views

app_name = "job"

urlpatterns = [

	path("", views.IndexView, name="index"),
	path("job-detail/<int:job_id>/", views.JobDetailView, name="job_detail"),
	path("apply-job/<int:job_id>/<int:app_user_id>/", views.ApplyJobView, name="apply_job"),
	path("my-applications/", views.MyApplicationsView, name="my_applications"),

	path("request-candiates/", views.RequestView, name="request"),
	path("manage-job/", views.ManageJobView, name="manage_job"),
	path("all-requests/", views.AllRequestsView, name="all_requests"),
	path("edit_request/<int:request_id>/", views.EditRequestView, name="edit_request"),
	path("request-detail/<int:request_id>/", views.RequestDetailView, name="request_detail"),
	path("assign/<int:request_id>/", views.AssignView, name="assign"),
	path("assign/<int:request_id>/<str:recruiter>/", views.Assign2View, name="assign2"),



	path("add-job/", views.AddJobView, name="add_job"),
	path("add-job-from-request/<int:request_id>/", views.AddJobFRView, name="add_job_fr"),

	path("job-applications/<int:job_id>/", views.JobApplicationsView, name="job_applications"),
	path("edit-job/<int:job_id>/", views.EditJobView, name="edit_job"),

	path("search-job/<str:query_type>/<str:query>/", views.SearchJobView, name="search_job"),
	path("all-location-jobs/<str:query>/", views.AllLocationView, name="all_location"),
	
]