from django import forms
from django.contrib.auth.models import UserLoginForm
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError


class UserLoginForm(forms.Form):
    """Form to be used to log users in"""

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(UserCreationForm):
    """ Form used to register new users """
    username = forms.CharField(label='Username',
                               min_length=6,
                               max_length=15,
                               widget=forms.TextInput(),
                               required=True)
    """ Email Address"""
    email = forms.CharField(label='Email Address',
                            min_length=6,
                            max_length=40,
                            widget=forms.EmailInput(),
                            required=True)
    """First Name"""
    first_name = forms.CharField(label='First Name',
                                 min_length=2,
                                 max_length=40,
                                 widget=forms.TextInput(),
                                 required=True)
    """ First Name"""
    last_name = forms.CharField(label='Last Name',
                                min_length=2,
                                max_length=40,
                                widget=forms.TextInput(),
                                required=True)
    """ First password entry"""
    password1 = forms.CharField(label="Password",
                                min_length=6,
                                max_length=25,
                                widget=forms.PasswordInput(),
                                required=True)
    """ Confirm password with a label"""
    password2 = forms.CharField(label="Repeat Password",
                                min_length=6,
                                max_length=25,
                                widget=forms.PasswordInput(),
                                required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name',
                  'last_name', 'password1', 'password2']