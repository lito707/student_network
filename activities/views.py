from django.shortcuts import render
from actstream.models import actor_stream, model_stream
from topics.models import Topic
# Create your views here.


def recent(request):

	# stream = actor_stream(request.user)
	# "user started following topic 4 2 minutes ago"
	stream = model_stream(request.user)

	template = "activities/recent.html"

	context = {
		"stream":stream
	}

	return render(request, template, context)
