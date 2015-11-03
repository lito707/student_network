from django.conf.urls import url
from . import views
from django.contrib.auth.views import login

# User URLs
urlpatterns = [
    url(r'^register/$',views.register, name = 'register'),
    url(r'^login/$', views.sign_in, name = 'login'),
    url(r'^logout', views.sign_out, name = 'logout'),
]
