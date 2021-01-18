from django.contrib import admin

from .models import StudentProfile, Courses, ProgramOfStudy

# Register your models here.
admin.site.register(StudentProfile)
admin.site.register(Courses)
admin.site.register(ProgramOfStudy)