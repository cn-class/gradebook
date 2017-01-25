from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('', 
#	url(r'^admin/', include(admin.site.urls)),
#	url(r'^home/$', 'homes.views.HomeView', name='home'),
	url(r'^$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
)

