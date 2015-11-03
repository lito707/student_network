from django.conf.urls import url
from . import views

# Topics URLs
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create', views.create, name='create'),
    url(r'^delete/(?P<topic_id>[0-9]+)/', views.delete, name='delete'),
    url(r'^topics_created', views.topics_created, name='topics_created'),
    url(r'^(?P<topic_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^follow_topic/$', views.my_follow, name='my_follow'),
    url(r'^unfollow_topic/$', views.my_unfollow, name='my_unfollow'),
    url(r'^following/$', views.my_following, name='my_following'),
    
]
