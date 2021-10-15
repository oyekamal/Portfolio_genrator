from django.db import models
from django.db.models.deletion import CASCADE


# Create your models here.
class UserEducation(models.Model):
    """
    models feild created for user education
    """

    qualification_name = models.CharField(max_length=50)
    completed_year = models.DateField() 
    user_percentage = models.PositiveIntegerField()
    user_CGPA = models.PositiveIntegerField()
    institute_location = models.CharField(max_length=100)