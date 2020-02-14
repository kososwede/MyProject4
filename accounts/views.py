from django.shortcuts import render, reverse, redirect, HttpResponseRedirect
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
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
    if request.user.is_authenticated():
        return redirect(reverse('index'))

    if request.method == "POST":
        login_form = UserLoginForm(request.POST)

        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully logged in to Unicorn Attractor!")

                 # Redirect user to home page once logged in
                if request.GET and request.GET['next'] != '':
                    next = request.GET['next']
                    return HttpResponseRedirect(next)
                else:
                    return redirect(reverse('profile'))
            else:
                login_form.add_error(None, "Your username or password is incorrect")
    else:
        login_form = UserLoginForm()

    args = {'login_form': login_form, 'next': request.GET.get('next', '')}
    
    return render(request, 'login.html', {'login_form': login_form})


def registration(request):
    """ Render the registration page """
    if request.user.is_authenticated():
        return redirect(reverse('index'))
    if request.method == 'POST':
        registration_form = UserRegistrationForm(request.POST)
        if registration_form.is_valid():
            registration_form.save()

            user = auth.authenticate(username=request.POST['username'], password=request.POST['password1'])

            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully registered and are now logged in to UNICORN ATTRACTOR")
            else:
                messages.error(request, "Unable to register at this time, Please try again")

    else:
        registration_form = UserRegistrationForm()

    return render(request, "registration.html", {"registration_form": registration_form})


def user_profile(request):
    """ Render the user profile page """
    user = User.objects.get(email=request.user.email)
    return render(request, 'profile.html', {'profile': user})