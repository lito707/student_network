from django.conf.urls import url
from . import views
# Topic URL
urlpatterns = [
    url(r'^$', views.home, name='home'),
]
