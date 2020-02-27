from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import TypeOfTicket, StatusOfTicket, Tickets, Comments, Upvote
from .forms import TicketForm, CommentForm, DonationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth.models import User
from accounts.models import Profile
import stripe
# Create your views here.
stripe.api_key = settings.STRIPE_SECRET

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


@login_required
def new_feature_ticket(request):
    '''user can create a new bug ticket'''
    if request.method == "POST":
        feature_form = TicketForm(request.POST)
        donation_form = DonationForm(request.POST)
        if feature_form.is_valid() and donation_form.is_valid():
            donation_amount = 0
            donation_amount += int(request.POST.get("donation_amount"))
            try:
                """ Use stripe's API to create a customer and charge them"""
                customer = stripe.Charge.create(
                    amount=int(donation_amount * 100),
                    currency="GBP",
                    description=request.user.email,
                    source=request.POST["stripeToken"]
                )
            except stripe.error.CardError:
                """ shows error message if the card is declined"""
                messages.error(request, "Your card has been declined!")

            """If the payment has been successful"""
            if customer.paid:
                feature_form.instance.user = request.user
                feature_form.instance.ticket_type_id = 2
                feature_form.instance.total_donations = donation_amount
                """ it will be Added to the user's total_donated amount
                and get the users current donations"""
                current_user_donated = Profile.objects.values_list(
                    "total_donated", flat=True).get(user_id=request.user.id)
                """ this will be added to the donated amount"""
                new_user_donated = current_user_donated + donation_amount
                """ The new amount will be added to the user's total donated amount"""
                Profile.objects.filter(user_id=request.user.id).update(
                    total_donated=new_user_donated)
                """ The status of the Ticket will be Working on if the user donates
                the target amount for the feature"""
                if donation_amount >= int(100):
                    feature_form.instance.ticket_status_id = 2
                else:
                    """ If the goal amount has not reached the target ammount, the status of the ticket will be Open"""
                    feature_form.instance.ticket_status_id = 1
                feature_form.save()
                messages.success(request, f"Thanks for submitting a Feature Request for Unicorn Attractor!")
                return redirect(get_tickets)
            else:
                messages.error(request, "Unable to take a payment at this time")
            """If the feature form or donation_form aren't valid"""
        else:
            messages.error(request, f"Sorry, We were unable to take a payment with that card. Please try again.")
    else:
        feature_form = TicketForm()
        donation_form = DonationForm()

    args = {
        "feature_form": feature_form,
        "donation_form": donation_form,
        "publishable": settings.STRIPE_PUBLISHABLE
    }

    return render(request, "new_feature.html", args)
