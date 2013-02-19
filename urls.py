from django.conf import settings
from django.conf.urls.defaults import patterns, include, url
#from django.views.generic.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
	# Examples:
	# url(r'^$', 'novembeard.views.home', name='home'),
	# url(r'^novembeard/', include('novembeard.foo.urls')),

	# Uncomment the admin/doc line below to enable admin documentation:
	# url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	
	# favicon.ico
	url(r'^favicon\.ico$', 'django.views.generic.simple.redirect_to', {'url': '/static/icons/favicon.ico'}),
#    (r'^favicon\.ico$', direct_to_template, {'template': '/static/icons/favicon.ico', 'mimetype': 'image/vnd.microsoft.icon'}),
	
	# robots.txt
	url(r'^robots\.txt$', 'django.views.generic.simple.redirect_to', {'url': '/static/robots.txt'}),
#    (r'^robots\.txt$', direct_to_template, {'template': '/static/robots.txt', 'mimetype': 'text/plain'}),

	# Uncomment the next line to enable the admin:
	url(r'^admin/', include(admin.site.urls)),
	
	# Catchall for now...
#	('^', direct_to_template, {'template': 'placeholder.html'}),
)

urlpatterns += patterns('web.views',
	# General
	url(r'^$', 'index', name='index'),
	url(r'^register/$', 'register', name='register'),
	url(r'^login/$', 'login', name='login'),
	url(r'^logout/$', 'logout', name='logout'),
	
	# Profile
	url(r'^profile/$', 'profile_edit', name='profile_edit'),
	url(r'^profile/(?P<profile_id>\w+)/$', 'profile_view', name='profile_view'),
	
	# Photo
	url(r'^profile/(?P<profile_id>\w+)/day/(?P<day>\d+)/$', 'photo_view', name='photo_view'),
	url(r'^photo/$', 'photo_add', name='photo_add'),
)

# STATIC and MEDIA files
if settings.DEBUG:
	urlpatterns += patterns('',
		url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
			'document_root': settings.STATIC_ROOT,
		}),
		url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
			'document_root': settings.MEDIA_ROOT,
		}),
   )
