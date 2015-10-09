from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^recent', views.recent, name='recent'),
]