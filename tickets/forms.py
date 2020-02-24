from django import forms
from .models import Tickets, Comments
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
        model = Tickets
        fields = ["title", "description"]


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
