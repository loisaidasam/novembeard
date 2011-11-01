import facebook as facebook
from web.models import Profile

from socialregistration.contrib.facebook.models import FacebookAccessToken, \
    FacebookProfile
from socialregistration.contrib.linkedin.models import LinkedInAccessToken, \
    LinkedInProfile, LinkedInRequestToken
from socialregistration.contrib.openid.models import OpenIDNonce, OpenIDProfile, \
    OpenIDStore
from socialregistration.contrib.twitter.models import TwitterAccessToken, \
    TwitterProfile, TwitterRequestToken


#def social_initial_data(request, user, profile, client):
#	'''
#	:param request: The current request object
#	:param user: The unsaved user object
#	:param profile: The unsaved profile object
#	:param client: The API client
#	'''
#	print "social_initial_data", request, user, profile, client


#def social_generate_username(user, social_profile, client):
#	'''
#	:param user: The unsaved user object
#	:param social_profile: The unsaved social_profile object
#	:param client: The API client
#	'''
#	# If user already exists we should be fine, right?
#	if user.username:
#		return user.username
#	
#	# First make a username based on what social network they logged in with
#	if social_profile.__class__.__name__ == 'FacebookProfile':
#		username = "fb_%s" % social_profile.uid
#	elif social_profile.__class__.__name__ == 'TwitterProfile':
#		username = "tw_%s" % social_profile.twitter_id
#	else:
#		try:
#			ex = "Unsupported social profile of type '%s' created!" % social_profile.__class__.__name__
#		except:
#			ex = "Unsupported social profile created!"
#		raise Exception(ex)
#	
##	# Then save the user
##	user.username = username
##	user.save()
##
##	# Create a profile for this object (only place we have this hook)
##	profile = Profile(user = user)
##	profile.save()
#
#	return username

