from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
    """
    Topic model with defined fields
    """
    topic_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now = False, auto_now_add = True)
    description = models.TextField()
    user = models.ForeignKey(User,null=True) 
    
    def get_fields(self):
        """
        Return all the fields the for a topic instance.
        """    
        fields = [self.topic_name, self.description]
        return fields

    def __str__(self):
        return self.topic_name

