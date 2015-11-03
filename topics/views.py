from .forms import TopicForm
from .models import Topic
from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponseBadRequest, Http404
from actstream.actions import follow, unfollow
from actstream.models import following, followers
from actstream import action
from resources.models import Resource

# Topics views

def index(request):
    """
    This handles the index of the topics existing returns a template with all 
    the topics and the ones the request user follows.
    """
    # check whether user is authenticated
    if request.user.is_authenticated():

        topics_list = Topic.objects.order_by('topic_name')
        # topics the user is following using the actstream following function
        following_list=  following(request.user) 

        context = {
            "topics_list":topics_list,
            "following_list":following_list,
        }
    else:
        topics_list = Topic.objects.order_by('topic_name')
        context = {
            "topics_list":topics_list,
        }

    template = 'topics/index.html'

    return render(request, template, context)


def detail(request, topic_id):
    """
    Check all the details for a topic with topic_id including the resources 
    added to it.
    """
    try:
        topic = Topic.objects.get(pk=topic_id)
        topic_resources = Resource.objects.filter(topic_id=topic_id)
    except Topic.DoesNotExist:
        raise Http404("ID not found")

    context ={
        "topic":topic,
        "topic_resources":topic_resources
    }
    template = 'topics/detail.html'

    return render(request, template, context)

# login required to created a topic
@login_required(login_url = '/users/login')
def create(request):
    """
    Create a topic 
    """
    #form where topic is created
    form = TopicForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        # check whether the topic name already exist 
        topic_exist = \
                (Topic.objects.filter(topic_name=instance.topic_name).exists())
        if not topic_exist:
            # If topic does not exist then create it
            instance.user_id = request.user.id
            instance.save()
            template = 'topics/create_success.html'
            # record the action performed a create action with the request user 
            # and a topic instance
            action.send(request.user, verb='created',target=instance)
            return render(request,template)            
    else:
        
        template = 'topics/create.html'
        context = {
            "form":form,
        }

        return render(request, template, context)


def topics_created(request):
    """
    Retrieves the topics created by the user who is making the request
    """
    user_id = request.user.id
    # In the topic model filter the ones with user_id
    topics_created = Topic.objects.filter(user_id=user_id)
    template="topics/topics_created.html"
    context={
        "topics_created":topics_created
    }

    return render(request,template,context)


def delete(request, topic_id):
    """
    Delete a topic by its ID
    """
    instance = Topic.objects.get(id=topic_id)
    instance.delete()
    template = "topics/delete_success.html"
    return render(request, template)

def my_follow(request):
    """ 
    Uses the follow function from the actstream library this takes an user 
    request and a topic by its ID and creates the follow relationship between
    user and topic.
    Returns a template with the successful action
    """
    if request.method == 'GET':        
        topic_id = request.GET.get('topic_id') #get topic id from the request
        if topic_id:
            topic_to_follow = Topic.objects.get(pk=topic_id)
            #user who makes the request
            req_user = User.objects.get(username=request.user) 
            #template to be rendered 
            template = 'topics/follow_success.html'
            follow(req_user, topic_to_follow, actor_only=False)
            return render(request, template)
        else:
            return HttpResponse("Follow cannot be processed")
    else:   
        return HttpResponse("Request cannot be processed")
    

def my_unfollow(request):
    """
    Use the unfollow from actstream to unfollow a topic 
    """
    if request.method == 'GET':        
        topic_id = request.GET.get('topic_id')
        if topic_id:
            topic_to_unfollow = Topic.objects.get(pk=topic_id)
            req_user = User.objects.get(username=request.user)        
            template = 'topics/unfollow_success.html'
            # user request to unfollow a topic 
            unfollow(req_user, topic_to_unfollow) 
            return render(request, template)
        else:
            return HttpResponse("Unfollow cannot be processed")

    else:
        return HttpResponse("Unfollow cannot be processed")


@login_required(login_url = '/users/login')
def my_following(request):
    """
    Render a list of the topics request user is currently following
    """
    following_list = []
    f_list=  following(request.user)
    for f in f_list:
        # check whether the topic still exists
        if f is not None:
            following_list.append(f)    
    template = "topics/following.html"
    context={
        "following_list":following_list,
    }
    return render(request, template, context)