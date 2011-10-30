from web.models import Profile, ProfileComment, Photo, PhotoComment, PhotoRating
from django.contrib import admin

admin.site.register(Profile)
admin.site.register(ProfileComment)
admin.site.register(Photo)
admin.site.register(PhotoComment)
admin.site.register(PhotoRating)