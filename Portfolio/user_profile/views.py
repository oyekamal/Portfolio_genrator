from django.shortcuts import render
from django.shortcuts import get_object_or_404, render

from .models import User
from education.models import UserEducation
from experiance.models import UserExperiance
from user_project.models import UserProject

def user_details(request):
    user = User.objects.get(username="kamal")
    education = UserEducation.objects.filter(user=user)
    experiance = UserExperiance.objects.filter(user=user)
    project = UserProject.objects.filter(user=user)


    print(education)
    print(experiance)
    print(project)
    return render(request, 'cv/index.html',{'user': user})


