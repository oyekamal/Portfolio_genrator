from django.db import models

from user_profile.models import User

# Create your models here.
class UserSkills(models.Model):
    """
    models feild created for user skills
    """
    skill_name = models.CharField(max_length=30,blank=True, null=True)
    skill_rate= models.DecimalField(max_digits=2 , decimal_places=0) 
    user = models.ForeignKey(User , on_delete = models.CASCADE, blank=True, null=True) 

    def __str__(self):
        return self.skill_name



# this need to be implementd