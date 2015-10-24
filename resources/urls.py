from django.conf.urls import url
from . import views

# Resources URL
urlpatterns = [
    # url(r'^$', views.index, name='index'),
    # url(r'^$', views.index, name='index'),
    url(r'^add_resource/(?P<topic_id>[0-9]+)/$', views.add_resource, name='add_resource'),
    # url(r'^delete', views.delete, name='delete'),
]
