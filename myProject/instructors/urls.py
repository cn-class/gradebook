from django.conf.urls import url
from django.core.urlresolvers import reverse
from .views import ( 
    HomeInstructorView, AnnounceInstructorView, 
	CheckInInstructorView, ShowAttendanceView, ShowGraphView, EditCourseView, AnnounceDetailView, 
    AnnounceSummarizeView, AddScoreView, SelectSectionView, EditSectionView, EditSectionInfoView )
from courses.views import (CourseView, SectionView, SectionSummarizeView, CourseInfoView, CourseSummarizeView, 
    SectionInfoView, AssessmentView,  SaveAssessmentView)
from accounts.views import EditInstructorProfileView, InstructorProfileView

urlpatterns = [
    url(r'^$', HomeInstructorView.as_view()),
    url(r'^announce-summarize/(?P<course_number>)/$', AnnounceSummarizeView.as_view()),
    url(r'^announce-detail', AnnounceDetailView.as_view()),
    url(r'^announce', AnnounceInstructorView.as_view()),
    
    url(r'^course/course-summarize', CourseSummarizeView.as_view()),
    url(r'^course/course-info', CourseInfoView.as_view()),
    url(r'^course/section-summarize', SectionSummarizeView.as_view()),
    url(r'^course/section-info', SectionInfoView.as_view()),  
    url(r'^course/section', SectionView.as_view()),
    url(r'^course/edit-assessment', AssessmentView.as_view()),
    url(r'^course/save-assessment', SaveAssessmentView.as_view()),
    url(r'^course', CourseView.as_view()),

    url(r'^editcourse/editsection-form', EditSectionInfoView.as_view()),
    url(r'^editcourse/select-section', EditSectionView.as_view()),
    url(r'^editcourse/section', SectionView.as_view()),
    url(r'^editcourse', EditCourseView.as_view()),

    url(r'^editprofile', EditInstructorProfileView.as_view()),
    url(r'^profile', InstructorProfileView.as_view()),

    url(r'^add-score', AddScoreView.as_view()),
    url(r'^checkin', CheckInInstructorView.as_view()),
    url(r'^showattendance', ShowAttendanceView.as_view()),
    url(r'^showgraph', ShowGraphView.as_view()),
    url(r'^select-section', SelectSectionView.as_view()),
]

