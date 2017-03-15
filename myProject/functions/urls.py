from django.conf.urls import url
from django.core.urlresolvers import reverse

from .views import AnnounceView, PredictView, CheckInView, PredictPopupView, HomeView, EnrollCourseView

urlpatterns = [
    #url(r'^$', FunctionView.as_view()),
    url(r'^$', HomeView.as_view()),
    url(r'^section4', HomeView.as_view()),
    url(r'^footer-area', HomeView.as_view()),
    url(r'^announce', AnnounceView.as_view()),
    url(r'^announce/predict', PredictView.as_view()),
    url(r'^predict/predictpopup', PredictPopupView.as_view()),
    url(r'^predict', PredictView.as_view()),
    url(r'^enrollcourse', EnrollCourseView.as_view()),
    url(r'^checkin', CheckInView.as_view()),
    

]
