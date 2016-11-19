from django.contrib import admin

from .models import Student
from .models import Instructor
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_filter = ('first_name','last_name','student_id','student_picture','major')
    search_fields = ['first_name','last_name','student_id','major']
    list_display = ('student_id','first_name','last_name','major','student_picture')

class InstructorAdmin(admin.ModelAdmin):
    list_filter = ('first_name','last_name','instructor_id','degree','instructor_picture','department')
    search_fields = ['first_name','last_name','instructor_id','department','degree']
    list_display = ('instructor_id','degree','first_name','last_name','department','instructor_picture')

admin.site.register(Student, StudentAdmin)
admin.site.register(Instructor, InstructorAdmin)
