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


def index(request):
#	print settings.STATIC_ROOT
	
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
	
	return render_to_response(
		'register.html', dict(
			facebook=FacebookProfile.objects.all(),
			twitter=TwitterProfile.objects.all(),
	), context_instance=RequestContext(request))


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
	return render_to_response('login.html', c)


def logout(request):
	user = request.user
	if user.is_authenticated():
		auth_logout(request)
	
	return redirect('index')
