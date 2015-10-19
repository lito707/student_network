from django.db import models
from topics.models import Topic
from django.contrib.auth.models import User

# Create your models here.
class Resource(models.Model):
    resource_name = models.CharField(max_length=100)
    url = models.URLField()
    description = models.TextField()
    resource_type = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now = False, auto_now_add = True)
    user = models.ForeignKey(User) 
    topic = models.ForeignKey(Topic)
    

    # use of email to perform activities
    # def get_fields(self):
    #     fields = [self.name, self.url, self. descriptionself.create_at, self.]
    #     # print "fields ",fields
    #     return fields


    def __str__(self):
        return self.resource_name
