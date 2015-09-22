from django.apps import AppConfig
from actstream import registry

class TopicsConfig(AppConfig):
    name = 'topics'

    def ready(self):
        registry.register(self.get_model('Topic'))
