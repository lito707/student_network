from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class MyUserRegistrationForm(UserCreationForm):
	"""
	Registration form to create users, using the UserCreationForm from
	the django authentication forms
	"""
	class Meta:
		"""
    	Model that the form uses
    	"""	
    	model = User
    	fields = ['first_name', 'last_name', 'username', 'email']

class MyUserLoginForm(AuthenticationForm):
	"""
	Login form to create users, using the AuthenticationForm from
	the django authentication forms
	"""
	class Meta:
		"""
		Model that the form uses
		"""
		model = User



  
