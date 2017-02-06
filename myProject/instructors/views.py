from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from courses.models import Course
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

        return render(request, self.template_name)

class CheckInInstructorView(TemplateView):
    template_name = 'checkInInstructor.html'

    def get(self, request):

        return render(request, self.template_name)

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

        return render(request, self.template_name)

    def post(self, request):
        context = {}
        course_number = request.POST.get("select_box")
        if course_number != None:
            queryset = Course.objects.get(course_number=course_number)
            context = {
                "obj": queryset,
                "course_number": course_number,

            }
            print (queryset)
            print ('\n')
        else:
            editcourse = request.POST.get("editcourse")
            if editcourse:
                course_number = request.POST.get('course_number')
                queryset = Course.objects.filter(course_number=course_number).update(
                    name=request.POST.get('name'),course_number=request.POST.get('course_number'), year=request.POST.get('year'),
                    semester=request.POST.get('semester'),description=request.POST.get('description'), major=request.POST.get('major'))
                # obj = Course(queryset)
            print (editcourse)
            print ('\n')
            print (course_number)
            print ('\n')
            print (queryset)
            print ('\n')
            
                # obj.name.value = request.POST.get('name')
                # obj.course_number.value = request.POST.get('course_number')
                # obj.year.value = request.POST.get('year')
                # obj.semester.value = request.POST.get('semester')
                # obj.description.value = request.POST.get('description')
                # obj.major.value = request.POST.get('major')
                # queryset.save()

        return render(request,self.template_name,context)
