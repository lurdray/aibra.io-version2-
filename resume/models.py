from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Title(models.Model):
	title = models.CharField(max_length=50, default="")

	status = models.BooleanField(default=False)
	pub_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.title



class OpeningStatement(models.Model):
	opening_statement = models.TextField(default="none")

	status = models.BooleanField(default=False)
	pub_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.opening_statement



class WorkExperience(models.Model):
	work_experience = models.CharField(max_length=50, default="none")
	company = models.CharField(max_length=50, default="none")
	detail = models.TextField(default="none")
	date_from = models.CharField(max_length=50, default="none")
	date_to = models.CharField(max_length=50, default="none")

	status = models.BooleanField(default=False)
	pub_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.work_experience



class Career(models.Model):
	career = models.TextField(default="none")
	detail = models.TextField(default="none")
	date_from = models.CharField(max_length=50, default="none")
	date_to = models.CharField(max_length=50, default="none")

	status = models.BooleanField(default=False)
	pub_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.career



class Education(models.Model):
	education = models.CharField(max_length=250, default="none")
	course = models.TextField(default="none")
	institution = models.CharField(max_length=500, default="none")
	date_from = models.CharField(max_length=50, default="none")
	date_to = models.CharField(max_length=50, default="none")

	status = models.BooleanField(default=False)
	pub_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.education


class Skill(models.Model):
	skill = models.CharField(max_length=50, default="none")
	detail = models.TextField(default="none")
	date_from = models.CharField(max_length=50, default="none")
	date_to = models.CharField(max_length=50, default="none")

	status = models.BooleanField(default=False)
	pub_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.skill



class Project(models.Model):
	project = models.CharField(max_length=50, default="none")
	detail = models.TextField(default="none")

	link = models.CharField(max_length=50, default="#")

	status = models.BooleanField(default=False)
	pub_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.project



class Involvement(models.Model):
	title = models.CharField(max_length=50, default="none")
	detail = models.TextField(default="none")

	link = models.CharField(max_length=50, default="#")

	status = models.BooleanField(default=False)
	pub_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.title



class Certification(models.Model):
	certification = models.CharField(max_length=50, default="none")
	detail = models.TextField(default="none")
	year = models.CharField(max_length=50, default="none")

	link = models.CharField(max_length=50, default="#")

	status = models.BooleanField(default=False)
	pub_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.certification



class Award(models.Model):
	award = models.CharField(max_length=50, default="none")
	detail = models.TextField(default="none")
	year = models.CharField(max_length=50, default="none")

	link = models.CharField(max_length=50, default="#")

	status = models.BooleanField(default=False)
	pub_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.award



class Hobby(models.Model):
	hobby = models.CharField(max_length=50, default="none")

	status = models.BooleanField(default=False)
	pub_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.hobby



class Referee(models.Model):
	referee = models.CharField(max_length=50, default="none")
	phone_no = models.CharField(max_length=50, default="none")
	email = models.CharField(max_length=50, default="none")
	place_of_work = models.TextField(max_length=50, default="none")

	status = models.BooleanField(default=False)
	pub_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.referee




class Resume(models.Model):

	str_tag = models.CharField(default="resume x", max_length=20)
	resume_cent = models.IntegerField(default=0)
	resume_status = models.BooleanField(default=False)
	work_experience_status = models.BooleanField(default=False)

	titles = models.ManyToManyField(Title, through="ResumeTitleConnector")
	opening_statements = models.ManyToManyField(OpeningStatement, through="ResumeOpeningStatementConnector")

	work_experiences = models.ManyToManyField(WorkExperience, through="ResumeWorkExperienceConnector")
	careers = models.ManyToManyField(Career, through="ResumeCareerConnector")
	educations = models.ManyToManyField(Education, through="ResumeEducationConnector")
	skills = models.ManyToManyField(Skill, through="ResumeSkillConnector")

	projects = models.ManyToManyField(Project, through="ResumeProjectConnector")
	involvements = models.ManyToManyField(Involvement, through="ResumeInvolvementConnector")
	certifications = models.ManyToManyField(Certification, through="ResumeCertificationConnector")
	awards = models.ManyToManyField(Award, through="ResumeAwardConnector")

	hobbies = models.ManyToManyField(Hobby, through="ResumeHobbyConnector")
	referees = models.ManyToManyField(Referee, through="ResumeRefereeConnector")

	status = models.BooleanField(default=False)
	pub_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.str_tag








class ResumeTitleConnector(models.Model):
	resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
	title = models.ForeignKey(Title, on_delete=models.CASCADE)
	pub_date = models.DateTimeField(default=timezone.now)

class ResumeOpeningStatementConnector(models.Model):
	resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
	opening_statement = models.ForeignKey(OpeningStatement, on_delete=models.CASCADE)
	pub_date = models.DateTimeField(default=timezone.now)

class ResumeWorkExperienceConnector(models.Model):
	resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
	work_experience = models.ForeignKey(WorkExperience, on_delete=models.CASCADE)
	pub_date = models.DateTimeField(default=timezone.now)

class ResumeCareerConnector(models.Model):
	resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
	career = models.ForeignKey(Career, on_delete=models.CASCADE)
	pub_date = models.DateTimeField(default=timezone.now)

class ResumeEducationConnector(models.Model):
	resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
	education = models.ForeignKey(Education, on_delete=models.CASCADE)
	pub_date = models.DateTimeField(default=timezone.now)

class ResumeSkillConnector(models.Model):
	resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
	skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
	pub_date = models.DateTimeField(default=timezone.now)


class ResumeProjectConnector(models.Model):
	resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
	project = models.ForeignKey(Project, on_delete=models.CASCADE)
	pub_date = models.DateTimeField(default=timezone.now)

class ResumeInvolvementConnector(models.Model):
	resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
	involvement = models.ForeignKey(Involvement, on_delete=models.CASCADE)
	pub_date = models.DateTimeField(default=timezone.now)

class ResumeCertificationConnector(models.Model):
	resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
	certification = models.ForeignKey(Certification, on_delete=models.CASCADE)
	pub_date = models.DateTimeField(default=timezone.now)

class ResumeAwardConnector(models.Model):
	resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
	award = models.ForeignKey(Award, on_delete=models.CASCADE)
	pub_date = models.DateTimeField(default=timezone.now)

class ResumeHobbyConnector(models.Model):
	resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
	hobby = models.ForeignKey(Hobby, on_delete=models.CASCADE)
	pub_date = models.DateTimeField(default=timezone.now)

class ResumeRefereeConnector(models.Model):
	resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
	referee = models.ForeignKey(Referee, on_delete=models.CASCADE)
	pub_date = models.DateTimeField(default=timezone.now)
