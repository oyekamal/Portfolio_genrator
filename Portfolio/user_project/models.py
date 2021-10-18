from django.db import models
from user_profile.models import User
# Create your models here.
class UserProject(models.Model):
    """
    models feild created for user project details
    """
    project_name = models.CharField(max_length=255)
    project_description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.project_name
