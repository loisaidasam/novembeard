from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
	user = models.OneToOneField(User, primary_key = True)
	vanity = models.CharField(max_length=16, blank=True, null=True)
	nickname = models.CharField(max_length=255, blank=True, null=True)
	bio = models.CharField(max_length=255, blank=True, null=True)
	
	def __unicode__(self):
		return '%s (nick: %s)' % (self.user, self.nickname)


class ProfileComment(models.Model):
	profile_user = models.ForeignKey(User, related_name='profile_user')
	commenter = models.ForeignKey(User, related_name='commenter', blank=True, null=True)
	commenter_ip = models.CharField(max_length=15)
	comment = models.CharField(max_length=255)
	published = models.DateTimeField(auto_now_add=True)


class Photo(models.Model):
	user = models.ForeignKey(User)
	day = models.IntegerField()
	caption = models.CharField(max_length=255, blank=True, null=True)
	published = models.DateTimeField(auto_now=True)
	views = models.IntegerField(default=0)
	
#	TODO: propagate saves to Stream model
#	def save(self, *args, **kwargs):
#		super(self.__class__, super).save(*args, **kwargs)
#			


class PhotoComment(models.Model):
	photo = models.ForeignKey(Photo)
	commenter = models.ForeignKey(User, blank=True, null=True)
	commenter_ip = models.CharField(max_length=15)
	comment = models.CharField(max_length=255)
	published = models.DateTimeField(auto_now_add=True)


class PhotoRating(models.Model):
	photo = models.ForeignKey(Photo)
	rater = models.ForeignKey(User, blank=True, null=True)
	rater_ip = models.CharField(max_length=15)
	rating = models.IntegerField(choices = ((-1, -1), (1, 1)))
	published = models.DateTimeField(auto_now_add=True)


# TODO: figure this out...
# example: "<img src='%s' /> %s commented on %s's photo: %s" % (image_link,
#	user1.get_profile().nickname, user2.get_profile().nickname, story_link)
#class Stream(models.Model):
#	image_link = models.CharField(max_length=255)
#	user1 = models.ForeignKey(User, related_name='user1')
#	user2 = models.ForeignKey(User, related_name='user2')
#	story_link = models.CharField(max_length=255)
#	story_template = models.CharField(max_length=255)
#	published = models.DateTimeField(auto_now_Add=True)


