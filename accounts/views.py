from django.shortcuts import render, reverse, redirect
from django.contrib import auth
# Create your views here.


def index(request):
    """ Returns the 'index.html' page """
    return render(request, 'index.html')


def logout(request):
    auth.logout(request)
    return redirect(reverse('index'))
