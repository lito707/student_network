from django.shortcuts import render
from forms import AddResourceForm
from actstream import action
from topics.models import Topic
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url = '/users/login')
def add_resource(request):
	
    
	form = AddResourceForm(request.POST or None)
	template = "resources/add_resource_form.html"

	
	if form.is_valid():
		instance = form.save(commit=False)
		topic_id = request.GET['topic_id']
		target_topic= Topic.objects.get(pk=topic_id)
		instance.topic_id = topic_id
		instance.user_id = request.user.id
		res_type = instance.type
		instance.save()
		context={}
		print "resource type was added "+ res_type
		action.send(request.user, verb=('added'+res_type),target=target_topic)
	else:

		context = {
            "form":form,
        }

	
	return render(request, template, context)