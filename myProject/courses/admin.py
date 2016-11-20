from django.contrib import admin

from .models import Course, Section, GradeCriteria, Enrollment, Assessment, Score, Attendance
# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_filter = ('id','name','course_number','year','semester','description','major')
    search_fields = ['name','course_number','year','semester','major']
    list_display = ('id','course_number','name','year','semester','major','description')

class SectionAdmin(admin.ModelAdmin):
    list_filter = ('id','section_number','year','semester','course_number','grade_criteria','time','instructor_id')
    search_fields = ['section_number','year','semester','course_number','time','instructor_id']
    list_display = ('id','section_number','year','semester','course_number','grade_criteria','time','instructor_id')

class GradeCriteriaAdmin(admin.ModelAdmin):
    list_filter = ('id','grade_criteria','range_start','range_end','grade')
    search_fields = ['grade_criteria','grade']
    list_display = ('id','grade_criteria','range_start','range_end','grade')

class EnrollmentAdmin(admin.ModelAdmin):
    list_filter = ('enrollment_id','student_id','section_number','grade')
    search_fields = ['enrollment_id','student_id','section_number','grade']
    list_display = ('enrollment_id','student_id','section_number','grade')

class AssessmentAdmin(admin.ModelAdmin):
    list_filter = ('assessment_id','section_number','assessment_type','max_point','weight','date')
    search_fields = ['assessment_id','section_number','assessment_type','date']
    list_display = ('assessment_id','section_number','assessment_type','max_point','weight','date')

class ScoreAdmin(admin.ModelAdmin):
    list_filter = ('id','enrollment_id','assessment_id','point')
    search_fields = ['id','enrollment_id','assessment_id','point']
    list_display = ('id','enrollment_id','assessment_id','point')

class AttendanceAdmin(admin.ModelAdmin):
    list_filter = ('id','enrollment_id','date','status')
    search_fields = ['id','enrollment_id','date','status']
    list_display = ('id','enrollment_id','date','status')

admin.site.register(Course, CourseAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(GradeCriteria, GradeCriteriaAdmin)
admin.site.register(Enrollment, EnrollmentAdmin)
admin.site.register(Assessment, AssessmentAdmin)
admin.site.register(Score, ScoreAdmin)
admin.site.register(Attendance, AttendanceAdmin)
