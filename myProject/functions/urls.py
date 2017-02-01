from django.conf.urls import url
from django.core.urlresolvers import reverse

from .views import AnnounceView, PredictView, CheckInView, PredictPopupView, HomeView

urlpatterns = [
    #url(r'^$', FunctionView.as_view()),
    url(r'^$', HomeView.as_view()),
    url(r'^announce', AnnounceView.as_view()),
    url(r'^announce/predict', PredictView.as_view()),
    url(r'^predictpopup', PredictPopupView.as_view()),
    url(r'^predict', PredictView.as_view()),
    #url(r'^function', FunctionView.as_view()),
    url(r'^checkin', CheckInView.as_view()),
    

]
