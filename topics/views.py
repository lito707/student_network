from django.shortcuts import render
from django.http import Http404
from .forms import TopicForm
from .models import Topic

# Create your views here.

def index(request):
    topics_list = Topic.objects.order_by('topic_name')
    print topics_list
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
    title = "Create Topic"
    template = 'topics/create.html'
    form = TopicForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        title = "Topic was created successfully"

        # change template
        context = {
            "title":title,
            # go back to the list or something
        }
    else:
        context = {
            "title":title,
            "form":form,

        }

    return render(request, template, context)
