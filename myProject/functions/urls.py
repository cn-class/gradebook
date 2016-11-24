from django.conf.urls import url
from django.core.urlresolvers import reverse

from .views import FunctionView, AnnounceView

urlpatterns = [
    url(r'^$', FunctionView.as_view()),
    url(r'^announce', AnnounceView.as_view()),
]
