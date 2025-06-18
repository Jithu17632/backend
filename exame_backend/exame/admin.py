from django.contrib import admin

# Register your models here.
from .models import ExamResult,Student

admin.site.register(ExamResult)
admin.site.register(Student)