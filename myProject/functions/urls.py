from django.conf.urls import url
from django.core.urlresolvers import reverse

from .views import FunctionView

urlpatterns = [
    #url(r'^$', HomeView.as_view()),
    url(r'^$', FunctionView.as_view()),

]
