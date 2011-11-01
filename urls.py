from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
	# Examples:
	# url(r'^$', 'novembeard.views.home', name='home'),
	# url(r'^novembeard/', include('novembeard.foo.urls')),

	# Uncomment the admin/doc line below to enable admin documentation:
	# url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	
	# Favicon
	url(r'^favicon\.ico$', 'django.views.generic.simple.redirect_to', {'url': '/static/images/favicon.ico'}),

	# Uncomment the next line to enable the admin:
	url(r'^admin/', include(admin.site.urls)),
	
	# Social Registration
	url(r'^social/', include('socialregistration.urls', namespace='socialregistration')),
	
	# Catchall for now...
#	('^', direct_to_template, {'template': 'placeholder.html'}),
)

urlpatterns += patterns('web.views',
	url(r'^$', 'index', name='index'),
	url(r'^register', 'register', name='register'),
	url(r'^login', 'login', name='login'),
	url(r'^logout', 'logout', name='logout'),
	
	url(r'^profile$', 'profile_edit', name='profile_edit'),
	url(r'^profile/(?P<profile>\w+)', 'profile_view', name='profile_view'),
	url(r'^profile/(?P<profile>\w+)/day/(?P<day>\d+)', 'photo_view', name='photo_view'),
	
	url(r'^photo$', 'photo_add', name='photo_add'),
	
#	(r'^polls/$', 'index'),
#	(r'^polls/(?P<poll_id>\d+)/$', 'detail'),
#	(r'^polls/(?P<poll_id>\d+)/results/$', 'results'),
#	(r'^polls/(?P<poll_id>\d+)/vote/$', 'vote'),
)