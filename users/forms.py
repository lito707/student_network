from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name']

    def clean_name(self):
        name = self.cleaned_data.get('name')
        return name
