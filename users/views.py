from django.shortcuts import render
from .forms import UserForm


# Create your views here.
def register(request):

    title = "Register"
    template = "users/register.html"
    form = UserForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        title = "Registration successful"
        context = {
            "title":title,
            "form": form,
        }
    else:
        context = {
            "title":title,
            "form": form,
        }
    return render(request, template, context)


def login(request):
    pass
