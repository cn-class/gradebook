from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

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