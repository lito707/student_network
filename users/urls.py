from django.conf.urls import url
from . import views

# User URLs
urlpatterns = [
    url(r'^register',views.register, name = 'register'),
]
