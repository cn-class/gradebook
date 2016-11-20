from django.contrib import admin

from .models import Course, Section
# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_filter = ('id','name','course_number','year','semester','description','major')
    search_fields = ['name','course_number','year','semester','major']
    list_display = ('id','course_number','name','year','semester','major','description')

class SectionAdmin(admin.ModelAdmin):
    list_filter = ('id','section_number','year','semester','course_number','grade_criteria','time','instructor_id')
    search_fields = ['section_number','year','semester','course_number','time','instructor_id']
    list_display = ('id','section_number','year','semester','course_number','grade_criteria','time','instructor_id')

admin.site.register(Course, CourseAdmin)
admin.site.register(Section, SectionAdmin)
