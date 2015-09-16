import datetime
from django.db import models
# from django.core.validators import URLValidator

# Create your models here.
class Resource(models.Model):
    rsrc_type = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now = False, auto_now_add = True)
    url = models.CharField(max_length=200)


    def __str__(self):
        return self.resource_text
