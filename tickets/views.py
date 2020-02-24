from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import TypeOfTicket, StatusOfTicket, Tickets, Comments, Upvote
from .forms import TicketForm, CommentForm

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
