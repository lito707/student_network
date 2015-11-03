from django import forms
from .models import Topic

class TopicForm(forms.ModelForm):
    topic_name = forms.CharField(label='Topic Name',required=True)
    description = forms.CharField(label='Description',widget=forms.Textarea,required=True)
  
    class Meta:
        model = Topic
        fields = ['topic_name', 'description']


    def clean_topic_name(self):
        topic_name = self.cleaned_data['topic_name']
        if (Topic.objects.filter(topic_name=topic_name).exists()):
            raise forms.ValidationError("Topic Name already exists!")

        # Always return the cleaned data, whether you have changed it or
        # not.
        return topic_name
    def __init__(self, *args, **kwargs):
        super(TopicForm, self).__init__(*args, **kwargs)

        for field in self.fields.values():
            field.error_messages = {'required':'The field {fieldname} is required'.format(
                fieldname=field.label)}