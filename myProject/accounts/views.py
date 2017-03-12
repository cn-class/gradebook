from django.core.urlresolvers import reverse
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Student, Instructor
from courses.models import Section
from django.contrib.auth.models import User,Group
from .forms import StudentForm, InstructorForm, EditInstructorProfileForm, InstructorProfileForm
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
            return HttpResponseRedirect('thankyou-student')
        else:
            return render(request, self.template_name, {'form': form})

class InstructorView(TemplateView):
    template_name = 'instructor.html'

    def get(self, request):
        form = InstructorForm()

        return render(request, self.template_name, {'form': form})

    def post(self, request):
        user = User()
        user.username = request.POST.get('instructor_id')
        user.first_name = request.POST.get('first_name')
        user.last_name =request.POST.get('last_name')
        user.email = request.POST.get('email')
        random_password = User.objects.make_random_password()
        user.set_password(random_password)
        user.save()
        instructor = Instructor()
        instructor.degree = request.POST.get('degree')
        instructor.first_name = request.POST.get('first_name')
        instructor.last_name = request.POST.get('last_name')
        instructor.instructor_id = request.POST.get('instructor_id')
        instructor.department = request.POST.get('department')
        instructor.save()
        group = Group.objects.get(name="Instructor")
        group.user_set.add(user)

        user_email = []
        user_email.append(user.email)
        user_username = user.username
        form = InstructorForm(data=request.POST)
        if form.is_valid():
            send_mail(
                '[Online Gradebook] Your Password', 
                'Your username: '+user_username+'\n'+'  Your password: '+random_password,
                settings.EMAIL_HOST_USER, 
                user_email, 
                fail_silently=False
            )
            return HttpResponseRedirect('/editors')
        else:
            return render(request, self.template_name, {'form': form})

class InstructorProfileView(TemplateView):
    template_name = 'instructorInfo.html'

    def get(self, request):
        if request.user.is_authenticated():
            username = request.user.username
        form = {}
        instructor_info = Instructor.objects.get(instructor_id=username) 
        course_lists = Section.objects.filter(instructor__instructor_id=instructor_info.instructor_id)
        print(course_lists)
        print('\n')
        form = InstructorProfileForm(obj=instructor_info)
        context = {
            "obj": instructor_info,
            "instructor_id": instructor_info.instructor_id,
            "course_lists": course_lists,
        }
        context['form'] = form

        return render(request,self.template_name,context)


class EditInstructorProfileView(TemplateView):
    template_name = 'editInstructorProfile.html'

    def get(self, request):
        if request.user.is_authenticated():
            username = request.user.username
        form = {}
        instructor_info = Instructor.objects.get(instructor_id=username) 

        form = EditInstructorProfileForm(obj=instructor_info)
        context = {
            "obj": instructor_info,
            "instructor_id": instructor_info.instructor_id
        }
        context['form'] = form

        return render(request,self.template_name,context)
        
    def post(self, request):
        queryset = {}
        current_instructor_id = request.POST.get('instructor_id')
        instructor_obj = Instructor.objects.get(instructor_id=current_instructor_id)
        queryset = Instructor.objects.filter(instructor_id=current_instructor_id).update(first_name=request.POST.get('first_name'),
            last_name=request.POST.get('last_name'), degree=request.POST.get('degree'), instructor_picture=request.POST.get('instructor_picture'), 
            department=request.POST.get('department'))
        userset = User.objects.filter(username=current_instructor_id).update(email=request.POST.get('email'),first_name=request.POST.get('first_name'),
            last_name=request.POST.get('last_name'))
        if queryset and userset:
            return HttpResponseRedirect('/instructors')


class ThankyouView(TemplateView):
    template_name = 'thankyou.html'

    def get(self, request):
        return render(request, self.template_name)


class ThankyouStudentView(TemplateView):
    template_name = 'thankyou_student.html'

    def get(self, request):
        return render(request, self.template_name)