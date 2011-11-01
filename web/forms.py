from django import forms
from django.utils.translation import gettext as _

from django.contrib.auth.models import User

from web.models import Profile

class RegisterForm(forms.Form):
	nickname = forms.CharField(max_length=255, required=False, help_text="(ie: Sammy Sandybeard)")
	email = forms.EmailField()
	password = forms.CharField(max_length=128, widget=forms.PasswordInput)
	
	def clean_email(self):
		email = self.cleaned_data.get('email')
		try:
			user = User.objects.get(email=email)
		except User.DoesNotExist:
			return email
		else:
			raise forms.ValidationError(_('This email is already in use in the system.'))

class LoginForm(forms.Form):
	email = forms.EmailField()
	password = forms.CharField(max_length=128, widget=forms.PasswordInput)
	

class UserForm(forms.Form):
	"""
	User creation form - for `SOCIALREGISTRATION_SETUP_FORM` setting.
	"""
	username = forms.RegexField(r'^\w+$', max_length=16, help_text="(ie: http://novembeard.org/profile/[your_username_here])")
	email = forms.EmailField()
	password = forms.PasswordInput()
	nickname = forms.CharField(max_length=255, required=False)
	bio = forms.CharField(max_length=255, required=False)


	def clean_username(self):
		username = self.cleaned_data.get('username')
		try:
			user = User.objects.get(username=username)
		except User.DoesNotExist:
			return username
		else:
			raise forms.ValidationError(_('This username is already in use.'))


	def save(self, request, user, social_profile, client):
		# Maybe we already have this user?
		if user.username:
			social_profile.user = user
			social_profile.save()
			return user, social_profile
		
		username = self.cleaned_data.get('username')
		user.username = username
		user.email = self.cleaned_data.get('email')
		user.password = self.cleaned_data.get('password')
		user.save()
		
		try:
			profile = user.profile
		except Profile.DoesNotExist:
			profile = Profile()
			profile.user = user
			profile.vanity = username
			profile.nickname = self.cleaned_data.get('nickname')
			profile.save()
		
		social_profile.user = user
		social_profile.save()
		return user, social_profile
