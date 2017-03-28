from django.shortcuts import (render, render_to_response,redirect)
from django.http import HttpResponseRedirect

from django.contrib.auth import (
	authenticate,
	get_user_model,
	login,
	logout,

	)
from django.contrib.auth.models import User,Group

from .forms import UserLoginForm, UserRegisterForm
# from django.contrib.auth.decorators import login_required
# from django.views.decorators.csrf import csrf_protect 
# from django.contrib import auth
# from django.core.context_processors import csrf
# import requests

# Create your views here.
def is_student(user):
	return user.groups.filter(name="Student").exists()

def is_instructor(user):
	return user.groups.filter(name="Instructor").exists()

def is_editor(user):
	return user.groups.filter(name="Editor").exists()

def login_view(request):
	# if request.user.is_authenticated:
	# 	return redirect("/home")

	title = "Login"
	form = UserLoginForm(request.POST or None) 
	if form.is_valid():
		username = form.cleaned_data.get('username')
		password = form.cleaned_data.get('password')
		user = authenticate(username=username, password=password)
		login(request, user)
		if is_student(user):
			return redirect("/home")
		elif is_instructor(user):
			return redirect("/instructors")
		elif is_editor(user):
			return redirect("/editors")
	return render(request, "login.html", {"form": form, "title": title})

def register_view(request):
	title = "Register"
	form = UserRegisterForm(request.POST or None)
	if form.is_valid():
		user = form.save(commit=False)
		password = form.cleaned_data.get('password')
		user.set_password(password)
		user.save()
		group = Group.objects.get(name="Student")
		group.user_set.add(user)
		new_user = authenticate(username=user.username,password=password)
		login(request, new_user)
		return redirect("/")
	context = {
		"form":form,
		"title":title,
	}

	return render(request, "form.html", context)


def logout_view(request):
	logout(request)
	return redirect("login")
