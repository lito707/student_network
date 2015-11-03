from django import forms
from .models import Resource


class AddResourceForm(forms.ModelForm):
	"""
	Form to add a resource
	"""
	url = forms.URLField(label='Link',required=True)
	resource_type = forms.CharField(label='Type',max_length=100)

	class Meta:
		# Model used in the form
		model = Resource
		fields = ['resource_name', 'url', 'description', 'resource_type']

	def __init__(self, *args, **kwargs):
		super(AddResourceForm, self).__init__(*args, **kwargs)

		# set the errors for the fields in the form
		for field in self.fields.values():
			field.error_messages = {'required':'The field {fieldname} is required'.format(
				fieldname=field.label)}