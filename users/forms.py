from django import forms
# from .models import User
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

class UserLoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
