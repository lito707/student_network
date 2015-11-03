from django.apps import AppConfig
from actstream import registry

class TopicsConfig(AppConfig):
	"""
	Configuration of topics app 
	"""
	name = 'topics'

	def ready(self):
		"""
		Register with the actstream library the model 
		where the relationships are to be created.
		"""
		# Register the Django User model 
		registry.register(self.get_model('Topic'))
