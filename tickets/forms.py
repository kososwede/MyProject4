from django import forms
from .models import Ticket, Comments
from datetime import datetime


class TicketForm(forms.ModelForm):
    """form allows users to create new tickets"""
    title = forms.CharField(
        label="Ticket Title",
        min_length=5,
        max_length=100,
        widget=forms.TextInput(),
        required=True)
    description = forms.CharField(
        label="Ticket Description",
        min_length=10,
        max_length=1500,
        widget=forms.Textarea(),
        required=True)

    class Meta:
        model = Ticket
        fields = ["title", "description"]


class DonationForm(forms.Form):
    '''users can select a donation amount
    its only used when adding or upvoting features
    users get a list of donation amounts, in multiples of 5'''
    DONATION_AMOUNT_CHOICES = [(i, i) for i in range(5, 105, 5)]

    donation_amount = forms.ChoiceField(
        label="Donation Amount",
        choices=DONATION_AMOUNT_CHOICES,
        required=False)


class CommentForm(forms.ModelForm):
    """Allows users to comment on any tickets"""
    description = forms.CharField(
        label="Comment",
        min_length=5,
        max_length=1500,
        widget=forms.Textarea(),
        required=True)

    class Meta:
        model = Comments
        fields = ["description"]
