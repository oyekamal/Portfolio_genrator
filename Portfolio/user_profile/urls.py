from django.urls import path

from . import views

app_name = 'store'

urlpatterns = [
    path('',views.user_details, name='user_details'),

]