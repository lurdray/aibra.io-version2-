from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from resume.models import Resume


class AppUser(models.Model):
    qr_photo = models.FileField(upload_to='account_files/profile_photos/', blank=True, default="default_files/default_face.jpg")
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account_type = models.CharField(default="candidate",max_length=10)

    cprofile_status = models.BooleanField(default=False)
    cv = models.FileField(upload_to='account_files/profile_photos/', blank=True, default="default_files/default_face.jpg")
    profile_photo = models.FileField(upload_to='account_files/profile_photos/', blank=True, default="default_files/default_face.jpg")
    address = models.TextField(default=" ")
    country = models.CharField(default=" ",max_length=100)
    postcode = models.CharField(default=" ",max_length=100, blank=True, null=True)
    language = models.CharField(default=" ",max_length=100, blank=True, null=True)
    job_category = models.CharField(default=" ",max_length=100, blank=True, null=True)
    city = models.CharField(default=" ",max_length=100, blank=True, null=True)
    experience = models.CharField(default=" ",max_length=100, blank=True, null=True)
    current_salary = models.CharField(default=" ",max_length=100, blank=True, null=True)
    expected_salary = models.CharField(default=" ",max_length=100, blank=True, null=True)
    phone_no = models.CharField(default=" ",max_length=15)
    age = models.CharField(default="dd/mm/yyyy",max_length=55)
    gender = models.CharField(default=" ",max_length=10)

    #socials
    facebook_link = models.CharField(default="",max_length=100, blank=True, null=True)
    twitter_link = models.CharField(default="",max_length=100, blank=True, null=True)
    instagram_link = models.CharField(default="",max_length=100, blank=True, null=True)
    linkedin_link = models.CharField(default="",max_length=100, blank=True, null=True)
    github_link = models.CharField(default="",max_length=100, blank=True, null=True)
    discord_link = models.CharField(default="",max_length=100, blank=True, null=True)


    #recruiters
    agency_name = models.CharField(default="",max_length=30, null=True)
    rank = models.CharField(default="1",max_length=30, null=True)
    ranks = models.CharField(default="1",max_length=30, null=True)
    rankers = models.CharField(default="1",max_length=30, null=True)
    charge = models.CharField(default="0",max_length=30, null=True)
    bio = models.TextField(default="This agency have not updated their bio..", null=True)
    agency_logo = models.FileField(upload_to='account_files/profile_photos/', blank=True, default="default_files/default_face.jpg")

    
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, null=True)

    otp_code = models.CharField(default="none",max_length=10)
    
    ec_status = models.BooleanField(default=False)
    status = models.BooleanField(default=False)
    
    #wallet shit
    wallet_address = models.CharField(default="null",max_length=100)
    wallet_key = models.CharField(default="null",max_length=100)
    
    pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user.username