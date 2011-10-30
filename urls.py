from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('web.views',
	(r'^register$', 'register'),
#	(r'^polls/$', 'index'),
#	(r'^polls/(?P<poll_id>\d+)/$', 'detail'),
#	(r'^polls/(?P<poll_id>\d+)/results/$', 'results'),
#	(r'^polls/(?P<poll_id>\d+)/vote/$', 'vote'),
)

urlpatterns += patterns('',
	# Examples:
	# url(r'^$', 'novembeard.views.home', name='home'),
	# url(r'^novembeard/', include('novembeard.foo.urls')),

	# Uncomment the admin/doc line below to enable admin documentation:
	# url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

	# Uncomment the next line to enable the admin:
	url(r'^admin/', include(admin.site.urls)),
	
	# Social Registration
	url(r'^social/', include('socialregistration.urls', namespace='socialregistration')),
	
	# Catchall for now...
	('^', direct_to_template, {'template': 'placeholder.html'}),
)
