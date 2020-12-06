from django.shortcuts import render, redirect
from django.http import request, HttpResponse
from .models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, authenticate
from django.contrib import messages


def index(request):

    if('username' not in request.session):
        return redirect('signin/')
    return render(request, 'index.html', {'title': 'Home'})


def signout(request):
    del request.session['username']
    return redirect('/')


def signin(request):
    if(request.method == 'POST'):
        username = request.POST.get('username')
        password = request.POST.get('password')
        if(username == "" and password == ""):
            return render(request, 'signin.html', {'username': 'Username is required', 'password': 'Password is required', 'title': 'SignIn'})
        elif(username == ""):
            return render(request, 'signin.html', {'username': 'Username is required', 'title': 'SignIn'})
        elif(password == ""):
            return render(request, 'signin.html', {'password': 'Password is required', 'title': 'SignIn'})
        elif(User.objects.filter(username=username.lower(), password=password).exists()):
            request.session['username'] = username.lower()
            return redirect('/')
    return render(request, 'signin.html', {'title': 'SignIn'})


def signup(request):
    if (request.method == "POST"):
        username = request.POST.get('username')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')

        if(username == "" and password == "" and cpassword == ""):
            return render(request, 'signup.html', {'username': 'Username is required', 'password': 'Password is required', 'title': 'SignUp'})
        elif(username == ""):
            return render(request, 'signup.html', {'username': 'Username is required', 'title': 'SignUp'})
        elif(User.objects.filter(username=username).exists()):
            return render(request, 'signup.html', {'username': 'Username not available', 'title': 'SignUp'})
        elif(password == ""):
            return render(request, 'signup.html', {'password': 'Password is required', 'title': 'SignUp'})
        elif(password != cpassword):
            return render(request, 'signup.html', {'password': 'Password not matching', 'title': 'SignUp'})
        else:
            User(username=username.lower(), password=password).save()
            return render(request, 'signup.html', {'status': 'SignUp Successfully', 'title': 'SignUp'})

    return render(request, 'signup.html', {'title': 'SignUp'})


def take(request, id):
    return HttpResponse("ID:  %s" % id)


def logout(request):
    logout(request)
    return redirect("main:home")
