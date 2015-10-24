from .forms import TopicForm
from .models import Topic
from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from actstream.actions import follow, unfollow
from actstream.models import following, followers
from actstream import action

# Topics views

def index(request):


    if request.user.is_authenticated():

        topics_list = Topic.objects.order_by('topic_name')
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
        # print instance.topic_name
        title = "Success"
        h1 = "Topic was created successfully"
        template = 'topics/create_success.html'
        # change template
        context = {
            "title":title,
            "h1":h1
            # go back to the list or something
        }
        action.send(request.user, verb='created',target=instance)
        print form
            
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


def my_follow(request):
    # topic = Topic.objects.get(pk=topic_id)
    # print request.user
    # template = 'topics/index.html'
    # context =  = RequestContext(request)

    # if request.user.is_authenticated and request.user.is_active
    if request.method == 'GET':        
        print "this is follow"
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

def my_unfollow(request):
    if request.method == 'GET':        
        print "this is unfollow"
        topic_id = request.GET['topic_id']
        topic_to_unfollow = Topic.objects.get(pk=topic_id)
        req_user_obj = User.objects.get(username=request.user)        
        template = 'topics/unfollow_success.html'
        unfollow(req_user_obj, topic_to_unfollow)
    else:
        print "not get", request    

    return render(request, template)


@login_required(login_url = '/users/login')
def my_following(request):
    print "this following",request.user 
    # req_usr = User.objects.get(username=request.user)
    # print req_usr
    following_list = []
    f_list=  following(request.user)
    for f in f_list:
        if f is not None:
            following_list.append(f)
    

    template = "topics/following.html"

    context={
        "following_list":following_list,
    }
    return render(request, template, context)