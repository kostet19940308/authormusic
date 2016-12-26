from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .views import *
from django.contrib import admin


urlpatterns = [
    url(r'^list/$', AlbumList.as_view(), name="list"),
    url(r'^(?P<pk>\d+)/$', AlbumView.as_view(), name="detail"),
    url(r'(?P<pk>\d+)/edit/$', EditAlbum.as_view(), name='album_edit'),
    url(r'^newalbum/$', login_required(CreateAlbum.as_view(), login_url=settings.LOGIN_URL), name='create_album'),
    url(r'(?P<pk>\d+)/edit/addtrack/$', AddTrack.as_view(), name='add_track'),
    url(r'(?P<album_id>\d+)/edit/(?P<pk>\d+)/edit$', EditTrack.as_view(), name='edit_track'),
]