from django.contrib import admin

from .models import Course
# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_filter = ('name','number','year','semester','description','major')
    search_fields = ['name','number','year','semester','major']
    list_display = ('number','name','year','semester','major','description')

admin.site.register(Course, CourseAdmin)
