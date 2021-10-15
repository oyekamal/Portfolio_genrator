from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    """
        user profile details of the user cv
    """

    personal_details = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='image/', default='image/default.jpg')
    content = models.PositiveIntegerField(blank=True,null=True)
    address = models.TextField(blank=True,null=True)