from django.db import models

# Create your models here.
class UserSkills(models.Model):
    """
    models feild created for user skills
    """
    skill_name = models.CharField(max_length=30)
    skill_rate= models.PositiveIntegerField()

    