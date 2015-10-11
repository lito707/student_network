from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^recent', views.recent, name='recent'),
    url(r'^follow_topic/$', views.my_follow, name='my_follow'),
    url(r'^following/$', views.my_following, name='my_following'),
]