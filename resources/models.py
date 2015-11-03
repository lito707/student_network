from django.db import models
from topics.models import Topic
from django.contrib.auth.models import User


class Resource(models.Model):
    """
    Resource model with defined fields
    """
    resource_name = models.CharField(max_length=100)
    url = models.URLField()
    description = models.TextField()
    resource_type = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now = False, auto_now_add = True)
    user = models.ForeignKey(User) 
    topic = models.ForeignKey(Topic)
    

    
    def get_fields(self):
        """
        Return all the fields the for a resource instance.
        """
        # set the errors for the fields in the form
        fields = [self.resource_name, self.url, self.description, self.resource_type, self.user]
        return fields

    def __str__(self):
        return self.resource_name
