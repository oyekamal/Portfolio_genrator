from django.shortcuts import render
from django.shortcuts import get_object_or_404, render

from .models import User

def user_details(request):
    user = User.objects.get(username="kamal")
    return render(request, 'cv/index.html',{'user': user})


