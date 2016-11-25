"""myProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from functions.views import CheckInView
from instructors.views import HomeInstructorView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^courses/', include('courses.urls')),
    url(r'^functions/', include('functions.urls')),
    url(r'^$', include('homes.urls')),
    url(r'^checkin', CheckInView.as_view() ,name="checkIn"),
    url(r'^instructors/', include('instructors.urls')),
    # url(r'^home/', include('homes.urls')),
    # url(r'^$', include('myProject.urls')),
]
