# Add your Facebook API keys here
FACEBOOK_APP_ID = '188147284599179'
FACEBOOK_SECRET_KEY = 'bb6f88e67800b1c73b159406d6c39855'
FACEBOOK_REQUEST_PERMISSIONS = ''

# Add your Twitter API keys here
TWITTER_CONSUMER_KEY = 'WeaPTprW4fpGqBhCvXjA'
TWITTER_CONSUMER_SECRET_KEY = 'eIu4RxTeTAKS79du98w6r0dI4OVEZHX22uHGXcn4M'

# Add your LinkedIn API keys here
LINKEDIN_CONSUMER_KEY = ''
LINKEDIN_CONSUMER_SECRET_KEY = ''

# Add your Github API keys here
GITHUB_CLIENT_ID = ''
GITHUB_CLIENT_SECRET = ''
GITHUB_REQUEST_PERMISSIONS = ''

# Add your Foursquare API keys here
FOURSQUARE_CLIENT_ID = ''
FOURSQUARE_CLIENT_SECRET = ''
FOURSQUARE_REQUEST_PERMISSIONS = ''

# Add your tumblr API keys here
TUMBLR_CONSUMER_KEY = ''
TUMBLR_CONSUMER_SECRET_KEY = ''


#def social_initial_data(request, user, profile, client):
#	'''
#	:param request: The current request object
#	:param user: The unsaved user object
#	:param profile: The unsaved profile object
#	:param client: The API client
#	'''
#	print "social_initial_data", request, user, profile, client


def social_generate_username(user, profile, client):
	'''
	:param user: The unsaved user object
	:param profile: The unsaved profile object
	:param client: The API client
	'''
	print "social_generate_username"
	print "user:", user
	print "profile:", profile
	print "client:", client
	return 'foo27'


SOCIALREGISTRATION_USE_HTTPS = False
SOCIALREGISTRATION_GENERATE_USERNAME = True
SOCIALREGISTRATION_GENERATE_USERNAME_FUNCTION = 'socialregistration.settings.social_generate_username'
#SOCIALREGISTRATION_INITIAL_DATA_FUNCTION = 'socialregistration.settings.social_initial_data'

LOGIN_REDIRECT_URL = '/'