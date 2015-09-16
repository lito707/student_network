from django import forms
from .models import Topic

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        # fields = ['topic_name', 'created_at', 'description']
        fields = ['topic_name', 'description']

        # def clean_topic_name(self):
        #     topic_name = self.cleaned_data.get('topic_name')
        #     return topic_name
        #
        # def clean_created_at(self):
        #     created_at = self.clean_created_at.get('created_at')
        #     return created_at
        #
        # def description(self):
        #     description = self.clean_description.get('description')
        #     return description
