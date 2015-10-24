from django.shortcuts import render
from forms import AddResourceForm
from actstream import action
from topics.models import Topic
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url = '/users/login')
def add_resource(request,topic_id):
	
    
	form = AddResourceForm(request.POST or None)
	template = "resources/add-resource-form.html"
	target_topic= Topic.objects.get(pk=topic_id)
	
	
	if form.is_valid():

		instance = form.save(commit=False)
		instance.topic_id = topic_id
		instance.user_id = request.user.id
		res_type = instance.resource_type
		instance.save()
		context={}
		# print "resource type was added "+ res_type
		action.send(request.user, verb=('added '+res_type+' to '),target=target_topic)
		template = "resources/add-success.html"
		print "add_success"
		return render(request, template, context)
	else:
		print "form not valid"
		
		print "errors", form.errors
	
		# template = "resources/errors.html"
		context = {
            "form":form,
            "following_topic":target_topic
        }

	
	return render(request, template, context)