from django.shortcuts import render
from actstream.models import actor_stream
from django.contrib.auth.models import User

# Create your views here.

def recent(request):

	stream = actor_stream(request.user)

	template = "activities/recent_activities.html"

	context = {
		"stream":stream
	}

	return render(request, template, context)
