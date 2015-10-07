from django.apps import AppConfig
from actstream import registry
class MyUsersConfig(AppConfig):
    name = 'myusers'

    def ready(self):
        registry.register(self.get_model('MyUser'))
