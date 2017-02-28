from django.conf.urls import url

from .views import AttendanceView, ScoreView, CourseView, AssessmentView, SectionView, EnrollmentView, GradeCriteriaView, CourseInfoView
from accounts.views import ThankyouView

urlpatterns = [
    #url(r'^$', IndexView.as_view()),
    url(r'^attendance', AttendanceView.as_view()),
    url(r'^score', ScoreView.as_view()),
    url(r'^course/course-info/(?P<course_number>)/$', CourseInfoView.as_view()), 
    url(r'^course', CourseView.as_view()),
    url(r'^assessment', AssessmentView.as_view()),
    url(r'^section', SectionView.as_view()),
    url(r'^enrollment', EnrollmentView.as_view()),
    url(r'^gradecriteria', GradeCriteriaView.as_view()),
    url(r'^thankyou/$', ThankyouView.as_view(), name='thankyou'),
]
