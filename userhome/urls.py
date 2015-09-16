from django.conf.urls import url
from . import views

# Topic URL
urlpatterns = [
    # url(r'^$', views.index, name='index'),
    url(r'^$', views.home, name='home'),
]
