from django.shortcuts import render
from django.http import Http404
from .forms import TopicForm
from .models import Topic
from django.contrib.auth.models import User

from actstream.actions import follow, unfollow
# Topics views

def index(request):
    topics_list = Topic.objects.order_by('topic_name')
    curr_user = request.user
    print "curr_user", curr_user
    print "id ", curr_user.id
    print "usr auth ", curr_user.is_authenticated()

    template = 'topics/index.html'
    context = {
        "topics_list":topics_list,
    }

    return render(request, template, context)


def detail(request, topic_id):
    template = 'topics/detail.html'
    try:
        topic = Topic.objects.get(pk=topic_id)
    except Topic.DoesnotExist:
        raise Http404("ID not found")

    return render(request, template, {"topic":topic})


def create(request):

    form = TopicForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
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
        title = "Create Topic"
        h1 = "Create Topic"
        template = 'topics/create.html'
        context = {
            "title":title,
            "form":form,

        }

    return render(request, template, context)

def follow(request):
    follow(request.user, group, actor_only=False)
    return
