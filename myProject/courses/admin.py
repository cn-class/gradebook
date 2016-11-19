from django.contrib import admin

from .models import Course, Section
# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_filter = ('name','number','year','semester','description','major')
    search_fields = ['name','number','year','semester','major']
    list_display = ('number','name','year','semester','major','description')

class SectionAdmin(admin.ModelAdmin):
    list_filter = ('number','year','semester','range_start','range_end','grade','time')
    search_fields = ['number','year','semester','time']
    list_display = ('number','year','semester','range_start','range_end','grade','time')

admin.site.register(Course, CourseAdmin)
admin.site.register(Section, SectionAdmin)
