from django.db import models

# Create your models here.
class UserProject(models.Model):
    """
    models feild created for user project details
    """
    project_name = models.CharField(max_length=30,blank=True, null=True)
    project_description = models.TextField()