from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect 
import requests

# Create your views here.

def home(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('./login.html', c)

def auth_view(request):
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	user = auth.authenticate(username=username, password=password)

	if user is not None:
		auth.login(request, user)
		return HttpResponseRedirect('/users/loggedin')
	else:
		return HttpResponseRedirect('/users/invalid')

def loggedin(request):
	return render_to_response('./loggedin.html', 
				 {'full_name': request.user.username})

def invalid_login(request):
	return render_to_response('./invalid_login.html')

def logout(request):
	auth.logout(request)
	return HttpResponseRedirect('/users/login')


