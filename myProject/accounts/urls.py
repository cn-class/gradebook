from django.conf.urls import url

from .views import StudentView, ThankyouView, InstructorView, ThankyouStudentView

urlpatterns = [
    #url(r'^$', IndexView.as_view()),
    url(r'^student', StudentView.as_view()),
    url(r'^instructor', InstructorView.as_view()),
    url(r'^thankyou/$', ThankyouView.as_view(), name='thankyou'),
    url(r'^thankyou-student/$', ThankyouStudentView.as_view(), name='thankyou_student'),
]
