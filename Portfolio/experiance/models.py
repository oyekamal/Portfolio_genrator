from django.db import models
from skill.models import UserSkills
# Create your models here.

class UserExperiance(models.Model):
    """
    model created for user experiance
    """
    job_title = models.CharField(max_length=255,blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    started_date = models.DateField()
    end_date = models.DateField()
    location = models.CharField(max_length=100,blank=True, null=True)
    # skills = models.ForeignKey(UserSkills , on_delete=models.CASCADE)