from django.apps import AppConfig
from actstream import registry
from django.contrib.auth.models import User

# registering models for activity stream library
class MyUsersConfig(AppConfig):
    name = 'myusers'

    def ready(self):
        # registry.register(self.get_model('MyUser'))
        registry.register(User)
