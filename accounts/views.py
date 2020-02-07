from django.shortcuts import render, reverse, redirect
from django.contrib import auth, messages
# Create your views here.


def index(request):
    """ Returns the 'index.html' page """
    return render(request, 'index.html')


def logout(request):
    """ Logs user out and displays a message """
    auth.logout(request)
    messages.success(request, "You have successfully been logged out of Unicorn Attractor")
    return redirect(reverse('index'))


def login(request):
    """ Logs user in """
    return render(request, 'login.html')
