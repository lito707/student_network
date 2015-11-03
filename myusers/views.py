from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from .forms import MyUserRegistrationForm, MyUserLoginForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm


def register(request):
    """
    Return a render template and context depending if a form is valid and a user
    registers successfully. If not successful registration return the error form
    """

    title = "Register"
    template = "myusers/register.html"
    form = MyUserRegistrationForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        title = "Registration successful"
        context = {
            "title":title,
            "registered":True
        }
    else:
        context = {
            "title":title,
            "form": form,
            "registered":False
        }
    return render(request, template, context)


def sign_in(request):
    """
    Render the template needed to login, context depends whether if the user can 
    successfully sign in. Redirect to home page if login is successful

    """

    h1=None
    template="myusers/login.html"
    form = MyUserLoginForm(request.POST or None)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            # check whether user is authenticated
            if user.is_active:
                # check whether user is active
                login(request, user)
                # redirect to home page
                return HttpResponseRedirect("/")
            else:
                h1 = "User not active"
        else:
            h1 = "Invalid login details"
    else:
        h1 = "Login"        
    context = {
        "form":form,
        "h1":h1
    }
    return render(request, template, context)


def sign_out(request):
    """
    Sign out a user making a request, redirect to home page after.
    """
    logout(request)
    
    return HttpResponseRedirect("/")
