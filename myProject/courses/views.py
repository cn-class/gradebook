from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Attendance, Score, Course, Assessment, Section, Enrollment, GradeCriteria
from accounts.models import Instructor
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
        
        name = request.POST.get('name')
        course_number = request.POST.get('course_number')
        year = request.POST.get('year')
        semester = request.POST.get('semester')
        description = request.POST.get('description')
        major = request.POST.get('major')
        request.session['name'] = name
        request.session['course_number'] = course_number
        request.session['year'] = year
        request.session['semester'] = semester
        request.session['description'] = description
        request.session['major'] = major
        

        return HttpResponseRedirect('/instructors/course/course-summarize/?course_number='+course_number)


class CourseSummarizeView(TemplateView):
    template_name = 'courseSummarize.html'
    def get(self, request):
        name = request.session.get('name')
        course_number = request.session.get('course_number')
        year = request.session.get('year')
        semester = request.session.get('semester')
        description = request.session.get('description')
        major = request.session.get('major')

        context = {
            "name": name,
            "course_number": course_number,
            "year": year,
            "semester": semester,
            "description": description,
            "major": major,
        }

        return render(request, self.template_name, context)

    def post(self, request):
        course = Course()
        course.name = request.POST.get('name')
        course.course_number = request.POST.get('course_number')
        course.year = request.POST.get('year')
        course.semester = request.POST.get('semester')
        course.description = request.POST.get('description')
        course.major = request.POST.get('major')
        course.save()

        return HttpResponseRedirect('/instructors/course/course-info/?course_number='+course.course_number)


class CourseInfoView(TemplateView):
    template_name = 'courseInfo.html'

    def get(self, request):
        course_number = request.GET.get('course_number')
        course_info = Course.objects.get(course_number=course_number)
    
        context = {
            "course_number": course_number,
            "course_info": course_info,
        }

        return render(request, self.template_name, context)


class SectionView(TemplateView):
    template_name = 'section.html'

    def get(self, request):
        context = {}
        queryset = {}
        form = {}
        course_number = request.GET.get('course_number')
        if course_number != None:
            queryset = Course.objects.get(course_number=course_number)
            form = SectionForm(obj=queryset)
            context = {
                "obj": queryset,
                "select_course_number": course_number,
            }
            context['form'] = form

            return render(request, self.template_name, {'form': form})
      
    def post(self, request):
        name = request.POST.get('name')
        course_number = request.POST.get('course_number')
        section_number = request.POST.get('section_number')
        time = request.POST.get('time')
        instructor_id = request.POST.get('instructor_id')
        instructor_info = Instructor.objects.get(instructor_id=instructor_id)
        year = request.POST.get('year')
        semester = request.POST.get('semester')
        description = request.POST.get('description')
        major = request.POST.get('major')

        request.session['name'] = name
        request.session['course_number'] = course_number
        request.session['section_number'] = section_number
        request.session['time'] = time
        request.session['instructor_id'] = instructor_id
        request.session['instructor_firstname'] = instructor_info.first_name
        request.session['instructor_lastname'] = instructor_info.last_name
        request.session['year'] = year
        request.session['semester'] = semester
        request.session['description'] = description
        request.session['major'] = major    

        return HttpResponseRedirect('/instructors/course/section-summarize/?course_number='+course_number)

class SectionSummarizeView(TemplateView):
    template_name = 'sectionSummarize.html'

    def get(self, request):
        name = request.session.get('name')
        course_number = request.session.get('course_number')
        section_number = request.session.get('section_number')
        time = request.session.get('time')
        instructor_id = request.session.get('instructor_id')
        first_name = request.session.get('instructor_firstname')
        last_name = request.session.get('instructor_lastname')
        year = request.session.get('year')
        semester = request.session.get('semester')
        description = request.session.get('description')
        major = request.session.get('major')

        context = {
            "name": name,
            "course_number": course_number,
            "section_number": section_number,
            "time": time,
            "instructor_id": instructor_id,
            "first_name": first_name,
            "last_name": last_name,
            "year": year,
            "semester": semester,
            "description": description,
            "major": major,
        }

        return render(request, self.template_name, context)

    def post(self, request):
        section = Section()
        course_number = request.POST.get('course_number')
        course_obj = Course.objects.get(course_number=course_number)
        section.section_number = request.POST.get('section_number')
        section.course = course_obj 
        section.year = request.POST.get('year')
        section.semester = request.POST.get('semester')
        # section.grade_criteria = request.POST.get('grade_criteria')
        section.time = request.POST.get('time')
        section.instructor_id = request.POST.get('instructor_id')
        section.save()
        section_id = str(section.id)
        assessment = Assessment(section_id=section.id,assessment_type="Midterm", max_point=0, weight=0, date=None)
        assessment.save()
        assessment = Assessment(section_id=section.id,assessment_type="Quiz1", max_point=0, weight=0, date=None)
        assessment.save()
        assessment = Assessment(section_id=section.id,assessment_type="Quiz2", max_point=0, weight=0, date=None)
        assessment.save()
        assessment = Assessment(section_id=section.id,assessment_type="Assignment", max_point=0, weight=0, date=None)
        assessment.save()
        assessment = Assessment(section_id=section.id,assessment_type="Final", max_point=0, weight=0, date=None)
        assessment.save()
        
        return HttpResponseRedirect('/instructors/course/section-info/?course_number='+course_number+'&section_id='+section_id) 


class SectionInfoView(TemplateView):
    template_name = 'sectionInfo.html'

    def get(self, request):
        course_number = request.GET.get('course_number')
        section_id = request.GET.get('section_id')
        section_info = Section.objects.get(id=section_id)
        course_info = section_info.course
        instructor_info = section_info.instructor
        assessment_info = Assessment.objects.filter(section__id=section_id)
        print(assessment_info)
        context = {
            "course_number": course_number,
            "course_info": course_info,
            "section_info": section_info,
            "instructor_info": instructor_info,
            "section_id": section_id, 
            "assessment_info": assessment_info,
        }

        return render(request, self.template_name, context)


class AssessmentView(TemplateView):
    template_name = 'assessment.html'

    def get(self, request):
        form = AssessmentForm()
        assessment_id = request.GET.get('assessment_id') 
        assessment_info = Assessment.objects.get(assessment_id=assessment_id)
        section_info = assessment_info.section
        context = {
            "assessment_info": assessment_info, 
            "section_info": section_info,
        }
        context['form'] = form

        return render(request, self.template_name, context)


class SaveAssessmentView(TemplateView):
    def post(self, request):
        assessment_id = request.POST.get("assessment_id")
        max_point = request.POST.get("max_point")   
        weight = request.POST.get("weight")
        date = request.POST.get("date")
        section_id = request.POST.get("section_id")

        queryset = Assessment.objects.filter(assessment_id=assessment_id).update(
            max_point=request.POST.get('max_point'),weight=request.POST.get('weight'), date=request.POST.get('date'))

        return HttpResponseRedirect('/instructors/course/section-info/?section_id='+section_id)

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
