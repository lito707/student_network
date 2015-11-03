from django.shortcuts import render
from forms import AddResourceForm
from actstream import action
from topics.models import Topic
from django.contrib.auth.decorators import login_required

@login_required(login_url = '/users/login')
def add_resource(request,topic_id):
	"""
	Returns a template for a POST request and a valid form, the resource is 
	added to a topic. Returns a template and context form to be filled otherwise
	
	topic_id: The ID of the topic which a resource is to be added.
	"""
	
	form = AddResourceForm(request.POST or None)
	template = "resources/add-resource-form.html"
	target_topic= Topic.objects.get(pk=topic_id)

	if form.is_valid() and request.POST:
		instance = form.save(commit=False)
		instance.topic_id = topic_id
		instance.user_id = request.user.id
		res_type = instance.resource_type
		res_name = instance.resource_name
		instance.save()
		action.send(request.user, verb=('added '+res_type+', '+res_name+' to'),
					target=target_topic)
		template = "resources/add-success.html"
		return render(request, template)
	else :
		context = {
            "form":form,
            "following_topic":target_topic
        }

	return render(request, template, context)