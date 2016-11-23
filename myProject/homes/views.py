from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

import requests

# Create your views here.
class HomeView(TemplateView):
    template_name = 'home.html'

    def get(self, request):

        return render(request, self.template_name)
