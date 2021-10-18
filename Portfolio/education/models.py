from django.db import models
from django.db.models.deletion import CASCADE
from user_profile.models import User

# Create your models here.
class UserEducation(models.Model):
    """
    models feild created for user education
    """

    qualification_name = models.CharField(max_length=50)
    completed_year = models.DateField() 
    user_percentage = models.DecimalField(max_digits=3, decimal_places=0)
    user_CGPA = models.DecimalField(max_digits=3, decimal_places=2)
    institute_location = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE,default="", null=True, blank=True)

    def __str__(self):
        return self.qualification_name