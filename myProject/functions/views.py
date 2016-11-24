from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

import requests

# Create your views here.
class FunctionView(TemplateView):
    template_name = 'function.html'

    def get(self, request):

        return render(request, self.template_name)

class AnnounceView(TemplateView):
    template_name = 'announce.html'

    def get(self, request):

        return render(request, self.template_name)
