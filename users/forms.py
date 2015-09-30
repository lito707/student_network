from django import forms
# from .models import User
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class UserRegistrationForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

class UserLoginForm(AuthenticationForm):

    class Meta:
        model = User



        # fields = ['username', 'password']
