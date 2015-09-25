from django.shortcuts import render
from django.contrib.auth import authenticate, login

from .forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.
def register(request):

    title = "Register"
    template = "users/register.html"
    form = UserRegistrationForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        print "isntace", instance
        instance.save()
        title = "Registration successful"
        context = {
            "title":title,
            # "form": form,
        }
    else:
        context = {
            "title":title,
            "form": form,
        }
    return render(request, template, context)

def sign_in(request):
    h1 = ""
    template = "users/login.html"
    form = UserLoginForm()
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                template = "users/login_success.html"
        else:
            h1 = "username or password incorrect"
    else:


        h1 = "Login"

    context = {
        "form":form,
        "h1":h1
    }


    return render(request, template, context)

def follow(request):
    return "follow from view"
