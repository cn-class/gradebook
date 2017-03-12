from django.conf.urls import url
from .views import HomeEditorView
from accounts.views import InstructorView

urlpatterns = [
    url(r'^$', HomeEditorView.as_view()),
    url(r'^create-instructors', InstructorView.as_view()),

]