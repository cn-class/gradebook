from django.conf.urls import url
from django.core.urlresolvers import reverse

from .views import ( HomeInstructorView, FunctionInstructorView, AnnounceInstructorView, 
	CheckInInstructorView, ShowAttendanceView, ShowGraphView, EditCourseView, AnnounceDetailView, AnnounceSummarizeView, AddScoreView )
from accounts.views import InstructorView
from courses.views import CourseView

urlpatterns = [
    url(r'^$', HomeInstructorView.as_view()),
    #url(r'^instructor', InstructorView.as_view()),
    url(r'^course', CourseView.as_view()),
    url(r'^editcourse', EditCourseView.as_view()),
    url(r'^functions', FunctionInstructorView.as_view()),
    url(r'^announce-summarize/(?P<course_number>)/$', AnnounceSummarizeView.as_view()),
    url(r'^announce-detail', AnnounceDetailView.as_view()),
    url(r'^announce', AnnounceInstructorView.as_view()),
    url(r'^add-score', AddScoreView.as_view()),
    url(r'^checkin', CheckInInstructorView.as_view()),
    url(r'^showattendance', ShowAttendanceView.as_view()),
    url(r'^showgraph', ShowGraphView.as_view()),
]

