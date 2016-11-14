from __future__ import unicode_literals

from django.conf import settings
from django.db import models

# Create your models here.

class Album(models.Model):
    name = models.CharField(max_length = 100)
    genre = models.CharField(max_length=100)

    author = models.ForeignKey('core.User', related_name='albums')

    created_in = models.DateTimeField(auto_now_add=True)

    photo = models.ImageField(upload_to='albums', blank=True, null=True)
    information = models.TextField(null=True, blank=True)


    def count_horns(self):
        return self.horns.count()

    def get_comments(self):
        return self.comments

    def get_tracks(self):
        return self.tracks

    def get_absolute_url(self):
        return '/albums/%i/' % self.id

# analogue for Likes
class Horns(models.Model):
    album = models.ForeignKey('Album', related_name='horns')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='horns')

    class Meta:
        unique_together = ("album", "author")

class Track(models.Model):
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to='tracks')
    album = models.ForeignKey('Album',related_name='tracks')