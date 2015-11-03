from django.conf.urls import url
from . import views

# Resources URL
urlpatterns = [
    url(r'^add_resource/(?P<topic_id>[0-9]+)/$', views.add_resource, name='add_resource'),
]
