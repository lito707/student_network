from django import forms
from .models import Resource

class ResourceForm(forms.ModelForm):
	class Meta:
		model = Resource
		fields = ['resource_name', 'url', 'description', 'resource_type']
