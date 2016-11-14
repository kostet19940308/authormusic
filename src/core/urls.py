from django.conf.urls import url,include
from django.contrib import admin
from .views import *
from django.contrib.auth.views import login, logout, password_change
from django.contrib.auth.decorators import login_required
from django.conf import settings


urlpatterns = [
    url(r'^$',home, name='home'),
    url(r'^(?P<slug>\w+)/$', login_required(UserView.as_view(), login_url=settings.LOGIN_URL), name="user"),
    url(r'^accounts/login/$', login, name='login'),
    url(r'^accounts/logout/$', login_required(logout, login_url=settings.LOGIN_URL), {'next_page' : '/'}, name='logout'),
    url(r'^accounts/password_change/$',
        login_required(password_change, login_url=settings.LOGIN_URL),{'template_name':'registration/password_change.html', 'post_change_redirect':'/'},
        name='password_change'),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^accounts/register/$', RegisterView.as_view(), name='register'),
    url(r'^(?P<slug>\w+)/edit/$', login_required(UserEdit.as_view(), login_url=settings.LOGIN_URL), name="user_edit"),
]