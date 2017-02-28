from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response, redirect
from django.views.generic import TemplateView
from courses.models import Assessment, Score, Enrollment, Attendance, Course, Section
from courses.forms import EditCourseForm
from django.db.models import Q
import requests
import collections
from django.template.defaulttags import register


# Create your views here.
class HomeInstructorView(TemplateView):
    template_name = 'homeInstructor.html'

    def get(self, request):

        return render(request,self.template_name)




class FunctionInstructorView(TemplateView):
    template_name = 'functionInstructor.html'

    def get(self, request):

        return render(request, self.template_name)




class AnnounceInstructorView(TemplateView):
    template_name = 'announceInstructor.html'

    def get(self, request):
        context = {}
        
        queryset = Course.objects.all()
        context = {
            "object_list": queryset,

        }
    
        return render(request, self.template_name, context)



class SelectSectionView(TemplateView):
    template_name = 'selectSection.html'

    def get(self, request):
        context = {}
        select_course_number = request.GET.get("course_number")
        section_list = Section.objects.filter(course__course_number=select_course_number)

        context = {
            "section_list": section_list,

        }
    
        return render(request, self.template_name, context)



class AnnounceDetailView(TemplateView):
    template_name = 'announceDetail.html'

    def get(self, request):
        select_course_number = request.GET.get("course_number")
        select_section_number = request.GET.get("section_number")

        queryset = Assessment.objects.filter(section__course__course_number=select_course_number, section__section_number=select_section_number).order_by('date')
        enrollments = Enrollment.objects.filter(section__course__course_number=select_course_number, section__section_number=select_section_number).order_by('student__student_id')
    
        pointset = collections.OrderedDict()
  
        for obj in enrollments:
        
            scores =Score.objects.filter(enrollment=obj.enrollment_id).order_by('assessment__date') 
            student_scores = collections.OrderedDict()
            for score in scores:
                if score.point != None:
                    student_scores[score.assessment.assessment_type] = score.point
                elif score.point == None:
                    student_scores[score.assessment.assessment_type] = ""
            student_scores[obj.grade] = obj.grade
            pointset[obj.student.student_id] = student_scores

        context = {
            "object_list": queryset,
            "enrollment_list": enrollments,
            "point_list": pointset,
            "select_course_number": select_course_number,
            "select_section_number": select_section_number,
        }

        return render(request,self.template_name,context)
 

    def post(self, request):
        select_course_number = request.POST.get("course_number")
        select_section_number = request.POST.get("section_number")
        ass_type = Assessment.objects.filter(section__course__course_number=select_course_number, section__section_number=select_section_number).order_by('date')
        enrollments = Enrollment.objects.filter(section__course__course_number=select_course_number, section__section_number=select_section_number).order_by('student__student_id')


        for obj in enrollments:
            for each in ass_type:
                point = request.POST.get(str(obj.student.student_id) +"_"+ each.assessment_type)
                if point == "":
                    point = 0
                    Score.objects.filter(enrollment__enrollment_id=obj.enrollment_id , assessment__assessment_id=each.assessment_id ).update(
                    point=point)
                    Enrollment.objects.filter(enrollment_id=obj.enrollment_id).update(grade=request.POST.get(str(obj.student.student_id) +"_"+ str(obj.grade)))
                else:
                    Score.objects.filter(enrollment__enrollment_id=obj.enrollment_id , assessment__assessment_id=each.assessment_id ).update(
                    point=point)
                    Enrollment.objects.filter(enrollment_id=obj.enrollment_id).update(grade=request.POST.get(str(obj.student.student_id) +"_"+ str(obj.grade)))
       
        return HttpResponseRedirect('/instructors/announce-summarize/?course_number='+select_course_number+'&section_number='+select_section_number)




class AnnounceSummarizeView(TemplateView):
    template_name = 'announceSummarize.html'

    def get(self, request):

        select_course_number = request.GET.get("course_number")
        select_section_number = request.GET.get("section_number")
        queryset = Assessment.objects.filter(section__course__course_number=select_course_number, section__section_number=select_section_number).order_by('date')
        enrollments = Enrollment.objects.filter(section__course__course_number=select_course_number, section__section_number=select_section_number).order_by('student__student_id')
        pointset = collections.OrderedDict()
        for obj in enrollments:
            scores =Score.objects.filter(enrollment=obj).order_by('assessment__date') 
            student_scores = collections.OrderedDict()
            for score in scores:
                student_scores[score.assessment.assessment_type] = score.point
 
            pointset[obj.student.student_id]=student_scores
       
        context = {
            "object_list": queryset,
            "student_list": enrollments,
            "point_list": pointset,
            "select_course_number": select_course_number,
            "select_section_number": select_section_number,
        }

        return render(request,self.template_name,context)




class AddScoreView(TemplateView):
    template_name = 'addScore.html'

    def get(self, request):
        select_course_number = request.GET.get("course_number")
        select_section_number = request.GET.get("section_number")
        split_obj = select_course_number.split('_')
        course_number = split_obj[0]
        ass_type = split_obj[1]

        context = {

            "ass_type": ass_type,
            "select_course_number": course_number,
            "select_section_number": select_section_number,
        }
        
        return render(request,self.template_name,context)

    def post(self,request):
        select_course_number = request.POST.get("course_number")
        select_section_number = request.POST.get("section_number")
        select_ass_type = request.POST.get("ass_type")
        input_score = request.POST.get("score")
        input_score = input_score.rstrip()
        ass_type = Assessment.objects.filter(section__course__course_number=select_course_number, section__section_number=select_section_number).order_by('date')
        student_score = input_score.split('\n')


        for score in student_score:
            each_student_score = score.split()
            enrollment = Enrollment.objects.get(section__course__course_number=select_course_number, section__section_number=select_section_number, student__student_id=each_student_score[0])
            Score.objects.filter(enrollment__enrollment_id=enrollment.enrollment_id, assessment__assessment_type=select_ass_type).update(point=each_student_score[1])
             
        return render(request,self.template_name)



class CheckInInstructorView(TemplateView):
    template_name = 'checkInInstructor.html'

    def get(self, request):
        course_number_query = Course.objects.all()

        context = {
            "course_number": course_number_query, 
        }

        return render(request,self.template_name,context)

    def post(self, request):
        select_course_number = request.POST.get("select_box")
        course_number_query = Course.objects.filter(~Q(course_number=select_course_number))

        context = {
            
            "course_number": course_number_query,
            "select_course_number": select_course_number,
        }

        return render(request,self.template_name,context)




class ShowAttendanceView(TemplateView):
    template_name = 'showAttendance.html'

    def get(self, request):

        return render(request, self.template_name)




class ShowGraphView(TemplateView):
    template_name = 'showGraph.html'

    def get(self, request):

        return render(request, self.template_name)




class EditCourseView(TemplateView):
    template_name = 'editcourse.html'
    def get(self, request):
        section_filter = request.GET.get("course_number")
        course_number_query = Course.objects.all()
        context = {
            "course_numbers": course_number_query, 
        }
        if section_filter == None:
            return render(request, self.template_name,context)
        else:
         
            return HttpResponseRedirect('/instructors/editcourse/section')

    def post(self, request):
        queryset = {}
        form = {}
        course_number = request.POST.get("select_box")       
        course_number_query = Course.objects.filter(~Q(course_number=course_number))
        if course_number != None:
            queryset = Course.objects.get(course_number=course_number)
            form = EditCourseForm(obj=queryset)
            context = {
                "obj": queryset,
                "course_number": course_number_query,
                "select_course_number": course_number,
            }
            context['form'] = form

            return render(request,self.template_name,context)
        else:
            course_number = request.POST.get('course_number')
            queryset = Course.objects.filter(course_number=course_number).update(
                name=request.POST.get('name'),course_number=request.POST.get('course_number'), year=request.POST.get('year'),
                semester=request.POST.get('semester'),description=request.POST.get('description'), major=request.POST.get('major'))
        
            if queryset :
                return HttpResponseRedirect('/instructors/editcourse')
        
