from django.shortcuts import render, reverse, redirect
from django.contrib import auth, messages
from accounts.forms import UserLoginForm

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
    if request.method == 'POST':
        login_form = UserLoginForm
    else:
        login_form = UserLoginForm()
    return render(request, 'login.html', {'login_form': login_form})
