from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):
    topic_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now = False, auto_now_add = True)
    description = models.TextField()
    user = models.ForeignKey(User) 
    

    # use of email to perform activities
    def get_fields(self):
        fields = [self.topic_name, self.description]
        # print "fields ",fields
        return fields

    def __str__(self):
        return self.topic_name

