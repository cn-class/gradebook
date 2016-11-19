from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Student
from .forms import StudentForm
import requests
# Create your views here.
class StudentView(TemplateView):
    template_name = 'home.html'

    def get(self, request):
        form = StudentForm()

        return render(request, self.template_name, {'student_form': form})

    def post(self, request):
        student = Student()
        student.first_name = request.POST.get('first_name')
        student.last_name = request.POST.get('last_name')
        student.student_id = request.POST.get('student_id')
        student.major = request.POST.get('major')
        student.save()

        form = StudentForm(data=request.POST)
        if form.is_valid():
            return HttpResponseRedirect(reverse('thankyou'))
        else:
            return render(request, self.template_name, {'student_form': form})

class ThankyouView(TemplateView):
    template_name = 'thankyou.html'

    def get(self, request):
        student = Student.objects.latest('student_id')
        return render(request, self.template_name, {'first_name': student.first_name,'last_name': student.last_name,'student_id': student.student_id, 'major': student.major})
        #return HttpResponse(student.name)
