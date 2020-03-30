from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from .forms import UserLoginForm, UserRegistrationForm, UserUpdateForm
from tickets.models import TicketModel

# Create your views here.


def index(request):
    """ Returns the 'index.html' page """
    return render(request, 'index.html')


def about(request):
    """Returns the 'about.html page """
    return render(request, 'about.html')


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
                auth.login(request=request, user=user)
                messages.success(request, "You have successfully logged in to Unicorn Attractor!")
                return redirect(reverse('profile'))
            else:
                messages.error(request, "Your username or password is incorrect")
    else:
        login_form = UserLoginForm()
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
                auth.login(request=request, user=user)
                messages.success(request, "You have successfully registered and are now logged in to UNICORN ATTRACTOR")

                return redirect(reverse('profile'))

            else:
                messages.error(request, "Unable to register at this time, Please try again")

    else:
        registration_form = UserRegistrationForm()

    return render(request, "registration.html", {"registration_form": registration_form})


@login_required
def user_profile(request):
    '''renders user's profile page and allows the user to update their User details and Profile image'''
    user_tickets = TicketModel.objects.filter(user_id=request.user.id)

    if request.method == "POST":
        user_form = UserUpdateForm(request.POST, instance=request.user)

        if user_form.is_valid():
            """ Save data if form is valid"""
            user_form.save()
            messages.success(request, "Your account at Unicorn Attractor has been successfully updated!")
            return redirect(reverse('profile'))

    else:
        user_form = UserUpdateForm(instance=request.user)

    args = {'user_form': user_form, 'user_tickets': user_tickets}
    return render(request, 'profile.html', args)
