from django import forms
from .models import Topic

class TopicForm(forms.ModelForm):
    """
    Form to add a topic
    """
    topic_name = forms.CharField(label='Topic Name',required=True)
    description = forms.CharField(label='Description',widget=forms.Textarea,required=True)
  
    class Meta:
        """
        Model used in the form
        """
        model = Topic
        fields = ['topic_name', 'description']


    def clean_topic_name(self):
        """
        Perform check in the topic name of the instance
        """
        topic_name = self.cleaned_data['topic_name']
        if (Topic.objects.filter(topic_name=topic_name).exists()):
            # check if topic name already exists
            raise forms.ValidationError("Topic Name already exists!")
        return topic_name

    def __init__(self, *args, **kwargs):
        super(TopicForm, self).__init__(*args, **kwargs)
        # set the errors for the fields in the form
        for field in self.fields.values():
            field.error_messages = {'required':'The field {fieldname} is required'.format(
                fieldname=field.label)}