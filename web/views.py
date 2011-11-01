from django.conf import settings
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext

from socialregistration.contrib.facebook.models import FacebookProfile
from socialregistration.contrib.twitter.models import TwitterProfile

from web.forms import UserForm


def index(request):
	user = request.user
	c = {
		'user': user
	}
	
	if user.is_authenticated():
		c['profile'] = user.get_profile()
	
	return render_to_response('index.html', c)


def register(request):
	user = request.user
	if user.is_authenticated():
		return redirect('index')
	
	c = {
		'user_form': UserForm, 
	}
	
	return render_to_response(
		'register.html', c,
		context_instance=RequestContext(request)
	)


def login(request):
	user = request.user
	if user.is_authenticated():
		return redirect('index')
	
	username = request.POST.get('username')
	password = request.POST.get('password')
	user = authenticate(username=username, password=password)
	
	if user is not None:
		# TODO: write some functionality for when users are not active
		if not user.is_active:
			pass
		else:
			auth_login(request, user)
			return redirect('index')
	
	c = {}
	return render_to_response('login.html', c,
		context_instance=RequestContext(request)
	)


def logout(request):
	user = request.user
	if user.is_authenticated():
		auth_logout(request)
	
	return redirect('index')


@login_required
def profile_edit(request):
	c = {}
	return render_to_response('profile_edit.html', c)


@login_required
def profile_view(request, profile_id):
	c = {}
	return render_to_response('profile_view.html', c)


@login_required
def photo_view(request, profile_id, day):
	c = {}
	return render_to_response('photo_view.html', c)


@login_required
def photo_add(request, profile_id):
	c = {}
	return render_to_response('photo_add.html', c)