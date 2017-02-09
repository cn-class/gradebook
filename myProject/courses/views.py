from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Attendance, Score, Course, Assessment, Section, Enrollment, GradeCriteria
from .forms import AttendanceForm, ScoreForm, CourseForm, AssessmentForm, SectionForm, EnrollmentForm, GradeCriteriaForm
import requests
# Create your views here.

class AttendanceView(TemplateView):
    template_name = 'attendance.html'

    def get(self, request):
        form = AttendanceForm()

        return render(request, self.template_name, {'attendance_form': form})

    def post(self, request):
        attendance = Attendance()
        attendance.enrollment_id = request.POST.get('enrollment_id')
        attendance.date = request.POST.get('date')
        attendance.status = request.POST.get('status')
        attendance.save()

        form = AttendanceForm(data=request.POST)
        if form.is_valid():
            return HttpResponseRedirect(reverse('thankyou'))
        else:
            return render(request, self.template_name, {'attendance_form': form})

class ScoreView(TemplateView):
    template_name = 'score.html'

    def get(self, request):
        form = ScoreForm()

        return render(request, self.template_name, {'score_form': form})

    def post(self, request):
        score = Score()
        score.enrollment_id = request.POST.get('enrollment_id')
        score.assessment_id = request.POST.get('assessment_id')
        score.point = request.POST.get('point')
        score.save()

        form = ScoreForm(data=request.POST)
        if form.is_valid():
            return HttpResponseRedirect(reverse('thankyou'))
        else:
            return render(request, self.template_name, {'score_form': form})

class CourseView(TemplateView):
    template_name = 'course.html'

    def get(self, request):
        form = CourseForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        course = Course()
        course.name = request.POST.get('name')
        course.course_number = request.POST.get('course_number')
        course.year = request.POST.get('year')
        course.semester = request.POST.get('semester')
        course.description = request.POST.get('description')
        course.major = request.POST.get('major')
        course.save()

        form = CourseForm(data=request.POST)
        if form.is_valid():
            return HttpResponseRedirect(reverse('thankyou'))
        else:
            return render(request, self.template_name, {'course_form': form})

class AssessmentView(TemplateView):
    template_name = 'assessment.html'

    def get(self, request):
        form = AssessmentForm()

        return render(request, self.template_name, {'assessment_form': form})

    def post(self, request):
        assessment = Assessment()
        assessment.section_number = request.POST.get('section_number')
        assessment.assessment_type = request.POST.get('assessment_type')
        assessment.max_point = request.POST.get('max_point')
        assessment.weight = request.POST.get('weight')
        assessment.date = request.POST.get('date')
        assessment.save()

        form = AssessmentForm(data=request.POST)
        if form.is_valid():
            return HttpResponseRedirect(reverse('thankyou'))
        else:
            return render(request, self.template_name, {'assessment_form': form})

class SectionView(TemplateView):
    template_name = 'section.html'

    def get(self, request):
        form = SectionForm()

        return render(request, self.template_name, {'section_form': form})

    def post(self, request):
        section = Section()
        section.section_number = request.POST.get('section_number')
        section.year = request.POST.get('year')
        section.semester = request.POST.get('semester')
        section.course_number = request.POST.get('course_number')
        section.grade_criteria = request.POST.get('grade_criteria')
        section.time = request.POST.get('time')
        section.instructor_id = request.POST.get('instructor_id')
        section.save()

        form = SectionForm(data=request.POST)
        if form.is_valid():
            return HttpResponseRedirect(reverse('thankyou'))
        else:
            return render(request, self.template_name, {'section_form': form})

class EnrollmentView(TemplateView):
    template_name = 'enrollment.html'

    def get(self, request):
        form = EnrollmentForm()

        return render(request, self.template_name, {'enrollment_form': form})

    def post(self, request):
        enrollment = Enrollment()
        enrollment.student_id = request.POST.get('student_id')
        enrollment.section_number = request.POST.get('section_number')
        enrollment.grade = request.POST.get('grade')
        enrollment.save()

        form = EnrollmentForm(data=request.POST)
        if form.is_valid():
            return HttpResponseRedirect(reverse('thankyou'))
        else:
            return render(request, self.template_name, {'enrollment_form': form})

class GradeCriteriaView(TemplateView):
    template_name = 'gradeCriteria.html'

    def get(self, request):
        form = GradeCriteriaForm()

        return render(request, self.template_name, {'gradeCriteria_form': form})

    def post(self, request):
        gradeCriteria = GradeCriteria()
        gradeCriteria.grade_criteria = request.POST.get('grade_criteria')
        gradeCriteria.range_start = request.POST.get('range_start')
        gradeCriteria.range_end = request.POST.get('range_end')
        gradeCriteria.grade = request.POST.get('grade')
        gradeCriteria.save()

        form = GradeCriteriaForm(data=request.POST)
        if form.is_valid():
            return HttpResponseRedirect(reverse('thankyou'))
        else:
            return render(request, self.template_name, {'gradeCriteria_form': form})
