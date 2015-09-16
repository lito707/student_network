from django.shortcuts import render
from .forms import ResourceForm
from .models import Resource

# Create your views here.
def create(request):

    title = "CREATE"
    form = ResourceForm(request.POST or None)

    context = {
        "title":title,
        "form":form,
        

    }

    return render(request, "users/register.html", context)

def index(request):

    pass

def delete(request):
    pass
