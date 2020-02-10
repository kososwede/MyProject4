from django.shortcuts import render, reverse, redirect
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
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
    if request.user.is_authenticated():
        return redirect(reverse('index'))
    if request.method == 'POST':
        login_form = UserLoginForm(request.POST)
        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])
            if user:
                auth.login(user=user, request=request)
                messages.success(request, 'Welcome back to Unicorn Attractor, You are now logged in!')
            else:
                login_form.add_error(None, 'Your Username or Password are incorrect, Please try again!')
    else:
        login_form = UserLoginForm()
    return render(request, 'login.html', {'login_form': login_form})
