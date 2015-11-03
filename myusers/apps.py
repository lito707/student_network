from django.apps import AppConfig
from actstream import registry
from django.contrib.auth.models import User


class MyUsersConfig(AppConfig):
	"""
	Configuration of myusers app 
	"""
	name = 'myusers'

	def ready(self):
		"""
		Register with the actstream library the model 
		where the relationships are to be created.
		"""
        # Register the Django User model 
		registry.register(User)
        
