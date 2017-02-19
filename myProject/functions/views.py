from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404,redirect,render_to_response
from django.views.generic import TemplateView
from courses.models import Assessment, Score, Enrollment, Attendance, Course
from accounts.models import Student, Instructor
from django.db.models import Q
import requests


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
        # print (selected_course_number)
        # print ('\n')
        all_sections = selected_course_number.section_set.all()
        # result='<option value="1">Test</option>'+"\n"
        for section in all_sections:
            result=result+'<option value="'+section.section_number+'">'+section.section_number+'</option>'+"\n"
            # print (section.section_number)
            # result_set.append({'section_number': section.section_number})
        # return HttpResponse(simplejson.dumps(result_set), mimetype='application/json',     content_type='application/json')
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
        print ('enter post')
        course_number = request.POST.get("selectcoursenumber")
        couse_info = Section.objects.get(course_number=course_number)
        username = None
        if request.user.is_authenticated():
            username = request.user.username
        user_info = Student.objects.get(student_id=username)
        
        # Score.objects.create(student=user_info.student_id)

        context = {
            "user_info": user_info,
            "course_info": course_info,
        }


        return render(request,self.template_name,context)

# class GetdetailsView(TemplateView):



       
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

        return render(request,'predictPopup.html',context)
        

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


    # def post(self, request):
    #     form = PredictForm(data=request.POST)
    #     if form.is_valid():
    #         return HttpResponseRedirect(reverse('function'))
    #     else:
    #         return render(request, self.template_name)


class PredictPopupView(TemplateView):
    template_name = 'predictPopup.html'
    def get(self, request):

        return render(request, self.template_name)
