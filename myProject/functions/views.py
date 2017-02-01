from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404,redirect,render_to_response
from django.views.generic import TemplateView
from courses.models import Assessment, Score, Enrollment
import requests


class HomeView(TemplateView):
    template_name = 'home.html'

    def get(self, request):

        return render(request, self.template_name)

"""class FunctionView(TemplateView):
    template_name = 'function.html'

    def get(self, request):

        return render(request, self.template_name)"""


class AnnounceView(TemplateView):
    template_name = 'announce.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        course_number = request.POST.get("select_box")
        queryset = Assessment.objects.filter(section__course__course_number=course_number).order_by('date')
        enrollments = Enrollment.objects.filter(section__course__course_number=course_number).order_by('student__student_id')
        pointset = []
        for obj in enrollments:
            pointset.append({'sid':obj.student.student_id,'scores':Score.objects.filter(enrollment=obj).order_by('assessment__date')})
                
        print (pointset)
        print ('\n')

        #for ps in pointset:
        #    for p in ps:
        #        print ("%s %s" % (ps.enrollment_id , ps.assessment_id))
        #        print (p.point)
        #        print ('\n')
        #print (queryset)
        #print (queryset[1].assessment_type)
        #print ('\n')

        context = {
            "object_list": queryset,
            "point_list": pointset,
            "course_number": course_number,
        }
        return render(request,self.template_name,context)



class PredictView(TemplateView):
    template_name = 'predict.html'

    def get(self, request):

        return render(request, self.template_name)

    def post(self, request):
        course_number = request.POST.get("select_box") 
        context = {
            
            "course_number": course_number,
        }
        return render(request,'predictPopup.html',context)
        


class CheckInView(TemplateView):
    template_name = 'checkIn.html'
    
    def get(self, request):
        return render(request, self.template_name)

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
