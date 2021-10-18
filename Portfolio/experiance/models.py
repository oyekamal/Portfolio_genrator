from django.db import models
from skill.models import UserSkills
from user_profile.models import User
# Create your models here.

class UserExperiance(models.Model):
    """
    model created for user experiance
    """
    job_title = models.CharField(max_length=255)
    description = models.TextField()
    started_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    location = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # skills = models.ForeignKey(UserSkills , on_delete=models.CASCADE)

    def __str__(self):
        return self.job_title
