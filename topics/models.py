from django.db import models
from django.apps import AppConfig
from actstream import registry
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):
    topic_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now = False, auto_now_add = True)
    description = models.TextField()
    


    # delete resources
    # decentralized (optional)
    # multiple users (how does an user2 see the system)
    # what does it do that other systems do not
    # because act streams are an open source
    #  push or pull notification system web socket

    # students if have questions such like stackoverflow how might they follow
    # such things

    # use of email to perform activities
    def get_fields(self):
        fields = [self.topic_name, self.description]
        # print "fields ",fields
        return fields

    def __str__(self):
        return self.topic_name
