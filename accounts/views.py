from django.shortcuts import render, reverse, redirect
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from accounts.forms import UserLoginForm, UserRegistrationForm

# Create your views here.


def index(request):
    """ Returns the 'index.html' page """
    return render(request, 'index.html')


@login_required
def logout(request):
    """ Logs user out and displays a message """
    auth.logout(request)
    messages.success(request, "You have successfully been logged out of Unicorn Attractor")
    return redirect(reverse('index'))


def login(request):
    """Return a login page"""
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)

        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully logged in to Unicorn Attractor!")
            else:
                login_form.add_error(None, "Your username or password is incorrect")
    else:
        login_form = UserLoginForm()
    return render(request, 'login.html', {'login_form': login_form})


def registration(request):
    """ Render the registration page """
    registration_form = UserRegistrationForm()
    return render(request, "registration.html", {"registration_form": registration_form})