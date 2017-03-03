from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404,redirect,render_to_response
from django.views.generic import TemplateView
from courses.models import Assessment, Score, Enrollment, Attendance, Course, Section
from accounts.models import Student, Instructor
from django.db.models import Q
import requests
import collections


class HomeView(TemplateView):
    template_name = 'home.html'
    def get(self, request):

        return render(request, self.template_name)


class EnrollCourseView(TemplateView):
    template_name = 'enrollCourse.html'
    def getdetails(course_number):
        result = ""
        all_sections = []
        answer = str(course_number[1:-1])
        selected_course_number = Course.objects.get(course_number=answer)
        all_sections = selected_course_number.section_set.all()
        for section in all_sections:
            result=result+'<option value="'+section.section_number+'">'+section.section_number+'</option>'+"\n"
        return result

    def get(self, request):
        if(request.GET.get('ajax')):
            course_number = request.GET.get('selectcoursenumber')
            return HttpResponse(EnrollCourseView.getdetails(course_number))
        else:
            course_number_query = Course.objects.all() 
            context = {
                "course_number": course_number_query, 
            }

            return render(request,self.template_name,context)
  
    def post(self, request):
        course_number = request.POST.get("selectcoursenumber")
        section_number = request.POST.get("selectsections")
        course_info = Section.objects.get(course__course_number=course_number, section_number=section_number)
        username = None

        if request.user.is_authenticated():
            username = request.user.username
        user_info = Student.objects.get(student_id=username)
        student_obj = Student.objects.get(student_id=user_info.student_id)
        section_obj = Section.objects.get(course__course_number=course_number, section_number=section_number)
        section_obj_pk = Section(section_obj.id)

        enroll = Enrollment.objects.create(student=student_obj,section=section_obj_pk,grade=None)
        ass_type = Assessment.objects.filter(section__course__course_number=course_number,section__section_number=section_number)

        for each in ass_type:
            enroll_score = Score.objects.create(enrollment=enroll,assessment=each,point=None)

        course_number = Course.objects.filter(~Q(course_number=course_number)) 

        context = {
            "user_info": user_info,
            "course_info": course_info,
            "course_number":  course_number,
        }

        return render(request,self.template_name,context)

 
class AnnounceView(TemplateView):
    template_name = 'announce.html'
    def get(self, request):
        course_number_query = Course.objects.all()

        context = {
            "course_number": course_number_query, 
        }

        return render(request,self.template_name,context)

    def post(self, request):
        select_course_number = request.POST.get("select_box")
        course_number_query = Course.objects.filter(~Q(course_number=select_course_number))  
        queryset = Assessment.objects.filter(section__course__course_number=select_course_number).order_by('date')
        enrollments = Enrollment.objects.filter(section__course__course_number=select_course_number).order_by('student__student_id')
        pointset = []
        for obj in enrollments:
            pointset.append({'sid':obj.student.student_id,'scores':Score.objects.filter(enrollment=obj).order_by('assessment__date')})

        context = {
            "object_list": queryset,
            "point_list": pointset,
            "course_number":  course_number_query,
            "select_course_number": select_course_number,
        }

        return render(request,self.template_name,context)


class PredictView(TemplateView):
    template_name = 'predict.html'

    def getdetails(course_number):
        result = ""
        all_sections = []
        answer = str(course_number[1:-1])
        selected_course_number = Course.objects.get(course_number=answer)
        all_sections = selected_course_number.section_set.all()
        for section in all_sections:
            result=result+'<option value="'+section.section_number+'">'+section.section_number+'</option>'+"\n"
        return result

    def get(self, request):
        if(request.GET.get('ajax')):
            course_number = request.GET.get('selectcoursenumber')
            return HttpResponse(EnrollCourseView.getdetails(course_number))
        else:
            course_number_query = Course.objects.all() 
            context = {
                "course_number": course_number_query, 
            }

            return render(request,self.template_name,context)


class PredictPopupView(TemplateView):
    template_name = 'predictPopup.html'

    def post(self, request):
        course_number = request.POST.get("selectcoursenumber")
        section_number = request.POST.get("selectsections")
        course_info = Section.objects.get(course__course_number=course_number, section_number=section_number)
        username = None
        if request.user.is_authenticated():
            username = request.user.username
        user_info = Student.objects.get(student_id=username)

        pointset = {}
        current_score = 0
        max_point = 0
        current_percentage = 0
        possible_score = 0
        totle_max_point = 0
        possible_totle_score = 0
        possible_grade = ''
        enrollments = Enrollment.objects.filter(student__student_id=user_info.student_id, section__course__course_number=course_number ,section__section_number=section_number)
        queryset = Assessment.objects.filter(section__course__course_number=course_number, section__section_number=section_number).order_by('date') 

        for obj in enrollments:
            scores =Score.objects.filter(enrollment=obj.enrollment_id).order_by('assessment__date') 
            assessment_list = {}
            student_scores = {}
            for score in scores:
                if score.point != None:
                    assessment_list[score.assessment.assessment_id] ={}
                    assessment_list[score.assessment.assessment_id][score.assessment.assessment_type] = score.point
                elif score.point == None:
                    assessment_list[score.assessment.assessment_id] ={}
                    assessment_list[score.assessment.assessment_id][score.assessment.assessment_type] = ""
            pointset[obj.student.student_id] = assessment_list 

        for sid,scores in pointset.items():
            for ass_id,score_obj in scores.items():
                for types,score in score_obj.items():
                    if int(score) > 0:
                        current_score += int(score)
                        for assessment in queryset:
                            if assessment.assessment_id == int(ass_id):
                                max_point += assessment.max_point

        for assessment in queryset:
            totle_max_point += assessment.max_point
        
        current_percentage = current_score*100/max_point
        possible_score = ((totle_max_point-max_point)/100)*current_percentage
        possible_totle_score = current_score+possible_score

        if possible_totle_score < 50:
            possible_grade = 'F'
        elif (possible_totle_score >= 50) and (possible_totle_score < 55):
            possible_grade = 'D'
        elif (possible_totle_score >= 55) and (possible_totle_score < 60):
            possible_grade = 'D+'
        elif (possible_totle_score >= 60) and (possible_totle_score < 65):
            possible_grade = 'C'
        elif (possible_totle_score >= 65) and (possible_totle_score < 70):
            possible_grade = 'C+'
        elif (possible_totle_score >= 70) and (possible_totle_score < 75):
            possible_grade = 'B'
        elif (possible_totle_score >= 75) and (possible_totle_score < 80):
            possible_grade = 'B+'
        elif (possible_totle_score >= 80) and (possible_totle_score <= totle_max_point):
            possible_grade = 'A'

        course_number_query = Course.objects.filter(~Q(course_number=course_number)) 

        context = {
            "user_info": user_info,
            "course_info": course_info,
            "course_number":  course_number,
            "course_number_query": course_number_query,
            "possible_grade": possible_grade,
        }

        return render(request, self.template_name, context)


class CheckInView(TemplateView):
    template_name = 'checkIn.html'  
    def get(self, request):
        course_number_query = Course.objects.all()

        context = {
            "course_number": course_number_query,
        }

        return render(request,self.template_name,context)

    def post(self, request):
        select_course_number = request.POST.get("select_box")
        course_number_query = Course.objects.filter(~Q(course_number=select_course_number))
        queryset = Attendance.objects.filter(enrollment__section__course__course_number=select_course_number)
        enrollments = Enrollment.objects.filter(section__course__course_number=select_course_number).order_by('student__student_id')
        attendanceset = []
        for obj in enrollments:
            attendanceset.append({'sid':obj.student.student_id, 'dates':Attendance.objects.filter(enrollment=obj).order_by('date'), 'status':Attendance.objects.filter(enrollment=obj).order_by('date')})

        context = {
            "object_list": queryset,
            "attendance_list": attendanceset,
            "course_number": course_number_query,
            "select_course_number": select_course_number,
        }

        return render(request,self.template_name,context)


