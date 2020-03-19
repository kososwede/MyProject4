from django import forms
from datetime import datetime
from .models import TicketModel, CommentModel


class FormForTickets(forms.ModelForm):
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
        max_length=2000,
        widget=forms.Textarea(),
        required=True)
        
    class Meta:
        model = TicketModel
        fields = ["title", "description"]


class DonationFormForTickets(forms.Form):
    '''users can select a donation amount its only used when adding or upvoting features users get a list of donation amounts'''
    DONATION_CHOICES = [(i, i) for i in range(10, 201, 10)]

    donation_amount = forms.ChoiceField(
        label="Donation Amount",
        choices=DONATION_CHOICES,
        required=False)


class CommentFormForTickets(forms.ModelForm):
    """Allows users to comment on any tickets"""
    description = forms.CharField(
        label="Comment Here",
        min_length=5,
        max_length=1500,
        widget=forms.Textarea(),
        required=True)

    class Meta:
        model = CommentModel
        fields = ["description"]
