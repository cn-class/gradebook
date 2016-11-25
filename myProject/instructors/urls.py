from django.conf.urls import url
from django.core.urlresolvers import reverse

from .views import HomeInstructorView, FunctionInstructorView, AnnounceInstructorView
from accounts.views import InstructorView
from courses.views import CourseView

urlpatterns = [
    url(r'^$', HomeInstructorView.as_view()),
    url(r'^instructor', InstructorView.as_view()),
    url(r'^course', CourseView.as_view()),
    url(r'^functions', FunctionInstructorView.as_view()),
    url(r'^announce', AnnounceInstructorView.as_view()),


]
