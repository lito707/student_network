from django.conf.urls import url
from . import views

# Topic URL
urlpatterns = [
    # url(r'^$', views.index, name='index'),
    url(r'^$', views.index, name='index'),
    url(r'^create', views.create, name='create'),
    url(r'^(?P<topic_id>[0-9]+)/$', views.detail, name='detail'),

]
