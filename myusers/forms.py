from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# class MyUserRegistrationForm(forms.ModelForm):
class MyUserRegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']

class MyUserLoginForm(AuthenticationForm):

    class Meta:
        model = User



        # fields = ['username', 'password']
