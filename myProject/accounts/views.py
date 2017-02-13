from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Student, Instructor
from .forms import StudentForm, InstructorForm
import requests
# Create your views here.

class StudentView(TemplateView):
    template_name = 'student.html'

    def get(self, request):
        form = StudentForm()

        return render(request, self.template_name, {'form': form})

    def post(self, request):
        student = Student()
        student.first_name = request.POST.get('first_name')
        student.last_name = request.POST.get('last_name')
        student.student_id = request.POST.get('student_id')
        student.major = request.POST.get('major')
        student.student_picture = request.POST.get('student_picture')
        student.save()

        form = StudentForm(data=request.POST)
        if form.is_valid():
            return HttpResponseRedirect(reverse('thankyou'))
        else:
            return render(request, self.template_name, {'student_form': form})

class InstructorView(TemplateView):
    template_name = 'instructor.html'

    def get(self, request):
        form = InstructorForm()

        return render(request, self.template_name, {'form': form})

    def post(self, request):
        instructor = Instructor()
        instructor.degree = request.POST.get('degree')
        instructor.first_name = request.POST.get('first_name')
        instructor.last_name = request.POST.get('last_name')
        instructor.instructor_id = request.POST.get('instructor_id')
        instructor.department = request.POST.get('department')
        instructor.save()

        form = InstructorForm(data=request.POST)
        if form.is_valid():
            return HttpResponseRedirect(reverse('thankyou'))
        else:
            return render(request, self.template_name, {'instructor_form': form})

class ThankyouView(TemplateView):
    template_name = 'thankyou.html'

    def get(self, request):
        student = Student.objects.latest('id')
        return render(request, self.template_name, {'first_name': student.first_name,'last_name': student.last_name,'student_id': student.student_id, 'major': student.major})
        #return HttpResponse(student.name)
