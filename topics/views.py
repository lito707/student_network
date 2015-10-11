from .forms import TopicForm
from .models import Topic
from django.shortcuts import render
from django.http import Http404, HttpResponse
from resources.models import Resource
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from actstream.registry import is_installed


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

def recent(request):
    from actstream.models import user_stream
    user = User.objects.get(pk=request.user.id)
    stream = user_stream(user, with_user_activity=True)

    template = "activities/recent_activities.html"

    context = {
        "stream":stream
    }

    return render(request, template, context)