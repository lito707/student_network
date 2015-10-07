from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from .forms import MyUserRegistrationForm, MyUserLoginForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.
def register(request):

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
            # "form": form,
        }
    else:
        context = {
            "title":title,
            "form": form,
            "registered":False
        }
    return render(request, template, context)


def sign_in(request):
    h1=""
    template=""
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                print "loggin"
                # template = "users/login_success.html"
                return HttpResponseRedirect("/")
            else:
                # User is not active
                h1 = "Invalid login details"
                template = "myusers/error.html"

        else:
            print "Invalid login details"
            h1 = "Invalid login details"


    else:
        # form is blank
        h1 = "Login"
        form = MyUserLoginForm()
        template = "myusers/login.html"
        print "not post"


    context = {
        "form":form,
        "h1":h1
    }


    return render(request, template, context)



# def redirect_to_sign_in(next, login_url = None,
#     redirect_field_name = REDIRECT_FIELD_NAME):
#
#     return ""

def sign_out(request):
    print "log out usr", request.user
    print "log out usr", request.user.id
    logout(request)
    print request.user.is_authenticated()
    
    return HttpResponseRedirect("/")
