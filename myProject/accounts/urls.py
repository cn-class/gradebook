from django.conf.urls import url

from .views import StudentView, ThankyouView

urlpatterns = [
    url(r'^$', StudentView.as_view()),
    url(r'^thankyou/$', ThankyouView.as_view(), name='thankyou'),
]
