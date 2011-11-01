from django.conf import settings
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext

from web.forms import LoginForm, RegisterForm
from web.models import Profile

def index(request):
	user = request.user
	c = {
		'user': user,
		'ga_account': settings.GA_ACCOUNT,
	}
	
	if user.is_authenticated():
		c['profile'] = user.get_profile()
	
	return render_to_response('index.html', c)


def register(request):
	user = request.user
	if user.is_authenticated():
		return redirect('index')
	
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			nickname = form.cleaned_data.get('nickname')
			email = form.cleaned_data.get('email')
			password = form.cleaned_data.get('password')
			
			user = User(email=email, username=email)
			user.set_password(password)
			user.save()
			
			profile = Profile(user=user, nickname=nickname)
			profile.save()
			
#			user = authenticate(username=email, password=password)
			auth_login(request, user)
			return redirect('index')
	else:
		form = RegisterForm() # An unbound form
	
	c = {
		'form': form,
		'ga_account': settings.GA_ACCOUNT,
	}
	
	return render_to_response(
		'register.html', c,
		context_instance=RequestContext(request)
	)


def login(request):
	user = request.user
	if user.is_authenticated():
		return redirect('index')
	
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			email = form.cleaned_data.get('email')
			password = form.cleaned_data.get('password')
			
			user = authenticate(username=email, password=password)
			
			# TODO: say "auth failed"
			if user is None:
				pass
			
			else:
				# TODO: say "user isn't active"
				if not user.is_active:
					pass
				
				else:
					auth_login(request, user)
					return redirect('index')
	else:
		form = LoginForm() # An unbound form
	
	c = {
		'form': form,
		'ga_account': settings.GA_ACCOUNT,
	}
	
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
	user = request.user
	c = {
		'user': user,
		'ga_account': settings.GA_ACCOUNT,
	}
	
	if user.is_authenticated():
		c['profile'] = user.get_profile()
	
	return render_to_response('profile_edit.html', c)


@login_required
def profile_view(request, profile_id):
	user = request.user
	c = {
		'user': user,
		'ga_account': settings.GA_ACCOUNT,
	}
	
	if user.is_authenticated():
		c['profile'] = user.get_profile()
	
	return render_to_response('profile_view.html', c)


@login_required
def photo_view(request, profile_id, day):
	user = request.user
	c = {
		'user': user,
		'ga_account': settings.GA_ACCOUNT,
	}
	
	if user.is_authenticated():
		c['profile'] = user.get_profile()
	
	return render_to_response('photo_view.html', c)


@login_required
def photo_add(request):
	user = request.user
	c = {
		'user': user,
		'ga_account': settings.GA_ACCOUNT,
	}
	
	if user.is_authenticated():
		c['profile'] = user.get_profile()
	
	return render_to_response('photo_add.html', c)