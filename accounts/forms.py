from django import forms


class UserLoginForm(forms.Form):
    """ Forms used to log users in """
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
