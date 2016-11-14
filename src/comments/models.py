from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Comment(models.Model):
    text = models.TextField()

    album = models.ForeignKey('albums.Album',related_name='comments')
    author = models.ForeignKey('core.User', related_name='his_comments')

    created_in = models.DateTimeField(auto_now_add=True)
