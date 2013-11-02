import datetime
from PIL import Image
import logging

logger = logging.getLogger(__name__)

from django.conf import settings
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext

from web.forms import LoginForm, RegisterForm, PhotoForm
from web.models import Profile, Photo

def index(request):
	user = request.user
	c = {
		'user': user,
		'ga_account': settings.GA_ACCOUNT,
	}
	
	if user.is_authenticated():
		c['profile'] = user.get_profile()
	
	c['photos'] = Photo.objects.all().order_by('-published')[:10]
	
	c['profiles'] = Profile.objects.all() 

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
			
			user = User(email=email, username=email[:30])
			user.set_password(password)
			user.save()
			
			profile = Profile(user=user, nickname=nickname)
			profile.save()

                        logger.info("New registration from %s/%s!", nickname, email)
			
#			user = authenticate(username=email, password=password)
#			auth_login(request, user)
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


def profile_view(request, profile_id):
	view_profile = Profile.objects.get(pk = profile_id)
	
	user = request.user
	c = {
		'user': user,
		'ga_account': settings.GA_ACCOUNT,
		'view_profile': view_profile,
		'photos': view_profile.user.photo_set.all().order_by("-day"),
	}
	
	if user.is_authenticated():
		c['profile'] = user.get_profile()
	
	return render_to_response('profile_view.html', c)


def photo_view(request, profile_id, day):
	user = request.user
	c = {
		'user': user,
		'ga_account': settings.GA_ACCOUNT,
	}
	
	if user.is_authenticated():
		c['profile'] = user.get_profile()
	
	try:
		try:
			photo_profile = Profile.objects.get(pk = profile_id)
			photo_user = User.objects.get(pk = photo_profile.user.id)
		except Profile.DoesNotExist:
			return redirect('index')
		except User.DoesNotExist:
			return redirect('index')
		
		photo = Photo.objects.get(user=photo_user, day=day)
	except Photo.DoesNotExist:
		return redirect('index')
	
	photo.views += 1
	photo.save()
	
	c['photo'] = photo
	c['photo_profile'] = photo_profile
	c['day'] = day
	
	return render_to_response('photo_view.html', c)


def handle_uploaded_file(f, user_id, day):
	accepted = ('image/jpg', 'image/jpeg')
	if f.content_type not in accepted:
		raise Exception("Invalid content type - only jpg files are accepted for uploading at this time")
	
	filename = '%s/beards/hi-res/%s_%s.jpg' % (settings.MEDIA_ROOT, user_id, day)
	destination = open(filename, 'wb+')
	for chunk in f.chunks():
		destination.write(chunk)
	destination.close()
	
	for folder, size in settings.IMAGE_SIZES.iteritems():
		im = Image.open(filename)
		im.thumbnail(size, Image.ANTIALIAS)
		im.save('%s/beards/%s/%s_%s.jpg' % (settings.MEDIA_ROOT, folder, user_id, day))


@login_required
def photo_add(request):
	user = request.user
	c = {
		'user': user,
		'ga_account': settings.GA_ACCOUNT,
	}
	if user.is_authenticated():
		c['profile'] = user.get_profile()
	
	if request.method == 'POST':
		form = PhotoForm(request.POST, request.FILES)
		if form.is_valid():
			try:
				day = form.cleaned_data.get('day')
				caption = form.cleaned_data.get('caption')
				
				handle_uploaded_file(request.FILES['photo'], user.id, day)
				
				try:
					photo = Photo.objects.get(user=user, day=day)
				except Photo.DoesNotExist:
					photo = Photo(
						user=user,
						day=day,
					)
				photo.caption = caption
				photo.save()
				
				return HttpResponseRedirect('/profile/%s/day/%s/' % (user.id, day))
			except Exception, e:
				logger.error("Exception when uploading a picture: %s" % e)
	else:
		today = datetime.date.today()
		form = PhotoForm(initial={'day': today.day})
	
	c['form'] = form
	
	return render_to_response('photo_add.html', c,
		context_instance=RequestContext(request)
	)
