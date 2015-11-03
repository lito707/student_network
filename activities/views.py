from django.shortcuts import render
from actstream.models import user_stream
from topics.models import Topic


def recent(request):
	"""
	Render the template showing recent activitiy of the user, using actstream 
	user_stream
	"""
	# retrieve the stream from an user
	stream = user_stream(request.user, with_user_activity=True)
	print stream
	template = "activities/recent.html"	
	context = {
		# show the latest 20 activities
		"stream":stream[:20]
	}

	return render(request, template, context)
