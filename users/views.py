from django.shortcuts import render
from django.contrib.auth import authenticate, login

from .forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth.models import User

# from django.contrib.auth.forms import UserCreationForm



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

def login(request):
    h1 = title = "Login"

    template = "users/login.html"
    # username = request.GET.get['username']
    # password = request.GET.get['password']
    #
    # user = authenticate(username = username, password = password)
    print "request method ", request.method
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        print "method is post"
        # user = authenticate(username = username, password = password)
        if form.is_valid():
            print "form is valid "
            username = form['username']
            password = form['password']
            user = authenticate(username = username, password = password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    template = "users/login_success.html"
            else:
                h1 = "Username or password incorrect",
        else:
            template = "users/error.html"
    else:
        form = UserLoginForm()

    context = {
        "title":title,
        "h1":h1,
        "form":form
    }


    return render(request, template, context)
