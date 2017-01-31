from django.contrib import admin

from .models import Course, Section, GradeCriteria, Enrollment, Assessment, Score, Attendance

from accounts.models import Student, Instructor
# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_filter = ('id','name','course_number','year','semester','description','major')
    search_fields = ['name','course_number','year','semester','major']
    list_display = ('id','course_number','name','year','semester','major','description')

class SectionAdmin(admin.ModelAdmin):
    list_filter = ('id','section_number','year','semester','course','time','instructor')
    search_fields = ['section_number','year','semester','course','time','instructor']
    list_display = ('id','section_number','year','semester','course_course_number','time','instructor_instructor_id')
    def course_course_number(self, obj):
        return obj.course.course_number
    def instructor_instructor_id(self, obj):
        return obj.instructor.instructor_id

class GradeCriteriaAdmin(admin.ModelAdmin):
    list_filter = ('id','section','range_start','range_end','grade')
    search_fields = ['section','grade']
    list_display = ('id','section_course','section_section_number','range_start','range_end','grade')
    def section_section_number(self, obj):
        return obj.section.section_number
    def section_course(self,obj):
        return obj.section.course.course_number


class EnrollmentAdmin(admin.ModelAdmin):
    list_filter = ('enrollment_id','student','section','grade')
    search_fields = ['enrollment_id','student_student_id','section_section_number','grade']
    list_display = ('enrollment_id','student_student_id','section_course','section_section_number','grade')
    def student_student_id(self, obj):
        return obj.student.student_id
    def section_section_number(self, obj):
        return obj.section.section_number
    def section_course(self,obj):
        return obj.section.course.course_number

class AssessmentAdmin(admin.ModelAdmin):
    list_filter = ('assessment_id','section','assessment_type','max_point','weight','date')
    search_fields = ['assessment_id','section','assessment_type','date']
    list_display = ('assessment_id','section_course','section_section_number','assessment_type','max_point','weight','date')
    def section_section_number(self, obj):
       return obj.section.section_number
    def section_course(self,obj):
       return obj.section.course.course_number

class ScoreAdmin(admin.ModelAdmin):
    list_filter = ('id','enrollment','assessment','point')
    search_fields = ['id','enrollment','assessment','point']
    list_display = ('id','enrollment_enrollment_id','assessment_assessment_id','point')
    def enrollment_enrollment_id(self, obj):
        return obj.enrollment.enrollment_id
    def assessment_assessment_id(self,obj):
        return obj.assessment.assessment_id

class AttendanceAdmin(admin.ModelAdmin):
    list_filter = ('id','enrollment','date','status')
    search_fields = ['id','enrollment','date','status']
    list_display = ('id','enrollment_enrollment_id','date','status')
    def enrollment_enrollment_id(self, obj):
        return obj.enrollment.enrollment_id

admin.site.register(Course, CourseAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(GradeCriteria, GradeCriteriaAdmin)
admin.site.register(Enrollment, EnrollmentAdmin)
admin.site.register(Assessment, AssessmentAdmin)
admin.site.register(Score, ScoreAdmin)
admin.site.register(Attendance, AttendanceAdmin)

