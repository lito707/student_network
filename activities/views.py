from django.shortcuts import render
from actstream.models import actor_stream, model_stream
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from actstream.actions import follow, unfollow
from actstream.models import following, followers
from actstream import action

# Create your views here.

def my_follow(request):
    # topic = Topic.objects.get(pk=topic_id)
    # print request.user
    # template = 'topics/index.html'
    # context =  = RequestContext(request)

    # if request.user.is_authenticated and request.user.is_active
    if request.method == 'GET':        
        topic_id = request.GET['topic_id']
        topic_to_follow = Topic.objects.get(pk=topic_id)
        req_user_obj = User.objects.get(username=request.user)        
        template = 'topics/follow_success.html'
        follow(req_user_obj, topic_to_follow, actor_only=False)
        # text = "this is follow"
        # print text
        # print "topics", is_installed(Topic)
        # print "users", is_installed(User)
        # print "group", is_installed(Group)
        # print "resources", is_installed(Resource)
    else:
        print "not get", request    

    return render(request, template)
    # return HttpResponse("This is follow")


@login_required(login_url = '/users/login')
def my_following(request):
    print "this following",request.user 
    # req_usr = User.objects.get(username=request.user)
    # print req_usr
    following_list =  following(request.user)
    template = "following.html"

    context={
        "following_list":following_list,
    }
    return render(request, template, context)




def recent(request):

	# stream = actor_stream(request.user)
	# "user started following topic 4 2 minutes ago"
	stream = model_stream(request.user)

	template = "activities/recent.html"

	context = {
		"stream":stream
	}

	return render(request, template, context)
