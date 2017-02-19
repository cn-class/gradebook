from django.shortcuts import (render, render_to_response,redirect)
from django.http import HttpResponseRedirect

from django.contrib.auth import (
	authenticate,
	get_user_model,
	login,
	logout,

	)

from .forms import UserLoginForm, UserRegisterForm
# from django.contrib.auth.decorators import login_required
# from django.views.decorators.csrf import csrf_protect 
# from django.contrib import auth
# from django.core.context_processors import csrf
# import requests

# Create your views here.


def login_view(request):
	print(request.user.is_authenticated)
	# if request.user.is_authenticated:
	# 	return redirect("/home")

	title = "Login"
	form = UserLoginForm(request.POST or None) 
	if form.is_valid():
		username = form.cleaned_data.get('username')
		password = form.cleaned_data.get('password')
		user = authenticate(username=username, password=password)
		login(request, user)
		return redirect("/home")
	return render(request, "login.html", {"form": form, "title": title})


def register_view(request):
	title = "Register"
	form = UserRegisterForm(request.POST or None)
	if form.is_valid():
		user = form.save(commit=False)
		password = form.cleaned_data.get('password')
		user.set_password(password)
		user.save()

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







# def home(request):
# 	c = {}
# 	c.update(csrf(request))
# 	return render_to_response('./login.html', c)

# def auth_view(request):
# 	username = request.POST.get('username', '')
# 	password = request.POST.get('password', '')
# 	user = auth.authenticate(username=username, password=password)

# 	if user is not None:
# 		auth.login(request, user)
# 		return HttpResponseRedirect('/users/loggedin')
# 	else:
# 		return HttpResponseRedirect('/users/invalid')


# def register_view(request):
# 	return render(request, "form.html", {})

# def loggedin(request):
# 	return render_to_response('./loggedin.html', 
# 				 {'full_name': request.user.username})

# def invalid_login(request):
# 	return render_to_response('./invalid_login.html')

# def register_view(request):
# 	return render(request,)

# def logout(request):
# 	auth.logout(request)
# 	return HttpResponseRedirect('/users/login')


