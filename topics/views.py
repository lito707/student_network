from django.shortcuts import render
from django.http import Http404, HttpResponse
from .forms import TopicForm
from .models import Topic
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from actstream.actions import follow, unfollow
from actstream.models import following, followers
from django.http import HttpResponseRedirect
# Topics views

def index(request):

    topics_list = Topic.objects.order_by('topic_name')
    template = 'topics/index.html'
    context = {
        "topics_list":topics_list,
    }

    return render(request, template, context)


def detail(request, topic_id):
    template = 'topics/detail.html'
    # print "detail",request.GET['topic_id']
    try:
        topic = Topic.objects.get(pk=topic_id)
    except Topic.DoesnotExist:
        raise Http404("ID not found")

    return render(request, template, {"topic":topic})


@login_required(login_url = '/users/login')
def create(request):

    form = TopicForm(request.POST or None)
    instance = form.save(commit=False)
    topic_exist = (Topic.objects.filter(topic_name=instance.topic_name).exists())
    if form.is_valid() and not topic_exist:
        
        instance.user_id = request.user.id
        instance.save()
        title = "Success"
        h1 = "Topic was created successfully"
        template = 'topics/create_success.html'
        # change template
        context = {
            "title":title,
            "h1":h1
            # go back to the list or something
        }
            
    else:
        template = 'topics/create.html'
        if topic_exist:
            h1 = title = "Topic name already exists!"

        else:
            title = "Create Topic"
            h1 = "Create Topic"
        
        
        context = {
            "title":title,
            "h1":h1,
            "form":form,
            "topic_exist":topic_exist
        }

    return render(request, template, context)   

def delete(request):
    instance = Topic.objects.get(id=topic_id)
    topic_name = instance.topic_name
    instance.delete()
    template = "topics/delete.html"
    context={
        "topic_name":topic_name
    }

    return render(request, template, context)


def follow_topic(request):
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
        text = "this is follow"
        print text
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