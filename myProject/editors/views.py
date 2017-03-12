from django.core.urlresolvers import reverse
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response, redirect
from django.views.generic import TemplateView
from accounts.models import Instructor
from django.contrib.auth.models import User,Group
from accounts.forms import InstructorForm
from courses.forms import EditCourseForm
from django.db.models import Q
import requests
import collections
from django.template.defaulttags import register

# Create your views here.
class HomeEditorView(TemplateView):
    template_name = 'homeEditor.html'

    def get(self, request):

        return render(request,self.template_name)
