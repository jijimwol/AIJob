from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Job,InterviewPractice

admin.site.register(Job)
admin.site.register(InterviewPractice)