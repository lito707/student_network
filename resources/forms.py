from django import forms
from .models import Resource

class AddResourceForm(forms.ModelForm):
	url = forms.URLField(label='Link',required=True)
	resource_type = forms.CharField(label='Type',max_length=100)

	class Meta:
		model = Resource
		fields = ['resource_name', 'url', 'description', 'resource_type']
