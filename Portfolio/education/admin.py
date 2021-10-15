from django.contrib import admin
from .models import UserEducation

# Register your models here.
# @admin.register()

# class adminBrand(admin.ModelAdmin):
#     user_education = UserEducation.objects.all()

admin.site.register(UserEducation)