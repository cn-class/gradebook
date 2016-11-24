from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
#
# from .forms import PredictForm
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

class PredictView(TemplateView):
    template_name = 'predict.html'

    def get(self, request):

        return render(request, self.template_name)

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
