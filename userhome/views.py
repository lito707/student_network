from django.shortcuts import render
# from topics.views import Create

# Create your views here.
def home(request):
    # url for create,
    template  = "home.html"
    return render(request, template)
