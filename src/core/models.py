from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

from django.urls import reverse
from django.utils.cache import caches

cache = caches['default']


class User(AbstractUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to='avatars', blank=True, null=True)
    email = models.EmailField(max_length=255)

    created_in = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('users:user',kwargs={'slug':self.username})

    def get_pubs(self):
        return self.albums

    def user_rating(self):
        key = 'rating_{}'.format(self.id)
        rating = cache.get(key)
        if rating is None:
            rating = 0
            for album in self.albums.all():
                rating += album.count_horns()
                rating += 3*album.count_buyers()
            cache.set(key, rating, 10)
        return rating