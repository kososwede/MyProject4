from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import TypeOfTicket, StatusOfTicket, Tickets, Comments, Upvote
from .forms import TicketForm, CommentForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth.models import User

# Create your views here.


def get_tickets(request):
    """ Return a list of tickets that were published prior to now
    and render them in the tickets.html page """
    tickets = Tickets.objects.all()
    type_of_ticket_dropdown = TypeOfTicket.objects.all()
    status_of_ticket_dropdown = StatusOfTicket.objects.all()

    """parameters"""
    TicketType = request.GET.get("TicketType")
    TicketStatus = request.GET.get("TicketStatus")

    """ filter by parameters"""
    if TicketType:
        tickets = tickets.filter(type_of_ticket__id=TicketType)
    else:
        tickets

    if TicketStatus:
        tickets = tickets.filter(status_of_ticket__id=TicketStatus)
    else:
        tickets

    args = {
        "tickets": tickets,
        "type_of_ticket_dropdown": type_of_ticket_dropdown,
        "status_of_ticket_dropdown": status_of_ticket_dropdown
    }

    return render(request, "get_tickets.html", args)


@login_required
def new_bug_ticket(request):
    '''user can create a new bug ticket'''
    if request.method == "POST":
        bug_form = TicketForm(request.POST)
        # This will save the form and redirect user to the page for corresponding ticket
        if bug_form.is_valid():
            bug_form.instance.user = request.user
            bug_form.instance.ticket_type_id = 1
            bug_form.instance.ticket_status_id = 1
            bug_form.save()
            messages.success(request, f"Thanks for making Unicorn Attractor better by submitting a Bug Report!")
            return redirect(get_tickets)

    else:
        bug_form = TicketForm()

    args = {
        "bug_form": bug_form
    }

    return render(request, "new_bug.html", args)
