from django.contrib import admin

from .models import Student
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_filter = ('first_name','last_name','student_id','student_picture','major')
    search_fields = ['first_name','last_name','student_id','major']
    list_display = ('student_id','first_name','last_name','major','student_picture')

admin.site.register(Student, StudentAdmin)
