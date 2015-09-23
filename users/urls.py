from django.conf.urls import url
from . import views

# User URLs
urlpatterns = [
    url(r'^register',views.register, name = 'register'),
    url(r'^login',views.sign_in, name = 'sign_in'),
    # url(r'^login', 'django.contrib.auth.views.login', {'template_name': 'users/login.html'})
]
