from django.shortcuts import render
# from topics.views import Create

# Create your views here.
def home(request):
    # url for create,
    template  = "userhome/home.html"
    title = "HOME"
    create_text = "Create Topic"

    context = {
        "title":title,
        "create_text":create_text,

    }
    return render(request, template, context)
