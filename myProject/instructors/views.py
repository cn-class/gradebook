from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from courses.models import Course
from django.db.models import Q
import requests


# Create your views here.
class HomeInstructorView(TemplateView):
    template_name = 'homeInstructor.html'

    def get(self, request):

        return render(request, self.template_name)


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

    def post(self, request):
        
        return render(request,self.template_name,context)


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
        course_number_query = Course.objects.all()

        context = {
            "course_number": course_number_query, 
        }

        return render(request, self.template_name,context)

    def post(self, request):
        context = {}
        course_number = request.POST.get("select_box")
        print (course_number)
        print ('\n')
        course_number_query = Course.objects.filter(~Q(course_number=course_number))
        if course_number != None:
            queryset = Course.objects.get(course_number=course_number)
        
            
        else:
            editcourse = request.POST.get("editcourse")
            if editcourse:
                course_number = request.POST.get('course_number')
                queryset = Course.objects.filter(course_number=course_number).update(
                    name=request.POST.get('name'),course_number=request.POST.get('course_number'), year=request.POST.get('year'),
                    semester=request.POST.get('semester'),description=request.POST.get('description'), major=request.POST.get('major'))
        
        context = {
                "obj": queryset,
                "course_number": course_number_query,
                "select_course_number": course_number,

        }

        return render(request,self.template_name,context)
