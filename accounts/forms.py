from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError


class UserLoginForm(forms.Form):
    """Form to be used to log users in"""

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(UserCreationForm):
    """ Form used to register new users """
    username = forms.CharField(label='  Username',
                               min_length=4,
                               max_length=20,
                               widget=forms.TextInput(),
                               required=True)
    """ Email Address"""
    email = forms.CharField(label='  Email Address',
                            min_length=6,
                            max_length=40,
                            widget=forms.EmailInput(),
                            required=True)
    """First Name"""
    first_name = forms.CharField(label='  First Name',
                                 min_length=1,
                                 max_length=40,
                                 widget=forms.TextInput(),
                                 required=True)
    """ Last Name"""
    last_name = forms.CharField(label='  Last Name',
                                min_length=1,
                                max_length=40,
                                widget=forms.TextInput(),
                                required=True)
    """ First password entry"""
    password1 = forms.CharField(label="  Password",
                                min_length=6,
                                max_length=25,
                                widget=forms.PasswordInput(),
                                required=True)
    """ Confirm password """
    password2 = forms.CharField(label="  Repeat Password",
                                min_length=6,
                                max_length=25,
                                widget=forms.PasswordInput(),
                                required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name',
                  'last_name', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')

        if User.objects.filter(email=email).exclude(username=username):
            raise forms.ValidationError(u'The email address you entered has already been registered.')
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if not password1 or not password2:
            raise ValidationError(u'Please confirm your password.')

        if password1 != password2:
            raise ValidationError(u'Passwords must match')

        return password2


class UserUpdateForm(forms.ModelForm):
    '''used to update the User model'''
    # Email Address
    email = forms.CharField(label='Email Address',
                            min_length=6,
                            max_length=40,
                            widget=forms.EmailInput(),
                            required=True)
    # First Name
    first_name = forms.CharField(label='First Name',
                                 min_length=1,
                                 max_length=40,
                                 widget=forms.TextInput(),
                                 required=False)
    # Last Name
    last_name = forms.CharField(label='Last Name',
                                min_length=1,
                                max_length=40,
                                widget=forms.TextInput(),
                                required=False)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']
