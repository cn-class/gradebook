from django.shortcuts import render
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect 
import requests

# Create your views here.

def home(request):
	return render(request, './templates/login.html')
	
