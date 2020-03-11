from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils import timezone
from accounts.models import Profile
from .models import TicketType, TicketStatus, TicketModel, UserComments, Upvote
from .forms import FormForTickets, CommentFormForTickets, DonationFormForTickets
import stripe

# Create your views here.
stripe.api_key = settings.STRIPE_SECRET


def get_tickets(request):
    """ Return a list of tickets that were published prior to now
    and render them in the tickets.html page """
    tickets = TicketModel.objects.all()
    
    ticket_type_dropdown = TicketType.objects.all()
    ticket_status_dropdown = TicketStatus.objects.all()

    """parameters"""
    ticket_type = request.GET.get("ticket_type")
    ticket_status = request.GET.get("ticket_status")

    """ filter by parameters"""
    if ticket_type:
        tickets = tickets.filter(ticket_type__id=ticket_type)
    else:
        tickets

    if ticket_status:
        tickets = tickets.filter(ticket_status__id=ticket_status)
    else:
        tickets

    args = {
        "tickets": tickets,
        "ticket_type_dropdown": ticket_type_dropdown,
        "ticket_status_dropdown": ticket_status_dropdown,
    }
  
    return render(request, "get_tickets.html", args)


@login_required
def new_bug(request):
    '''user can create a new bug ticket'''
    if request.method == "POST":
        bug_form = FormForTickets(request.POST)
        # This will save the form and redirect user to the page for corresponding ticket
        if bug_form.is_valid():
            bug_form.instance.user = request.user
            bug_form.instance.ticket_type_id = 1
            bug_form.instance.ticket_status_id = 1
            bug_form.save()
            messages.success(
                request, f"Thanks for making Unicorn Attractor better by submitting a Bug Report!")
            return redirect(get_tickets)

    else:
        bug_form = FormForTickets()

    args = {
        "bug_form": bug_form
    }

    return render(request, "new_bug.html", args)


@login_required
def new_feature(request):
    '''
    Allows user to create a new bug ticket
    '''
    if request.method == "POST":
        feature_form = FormForTickets(request.POST)
        donation_form = DonationFormForTickets(request.POST)
        if feature_form.is_valid() and donation_form.is_valid():
            donation_amount = 0
            donation_amount += int(request.POST.get("donation_amount"))
            try:
                customer = stripe.Charge.create(
                    amount=int(donation_amount * 200),
                    currency="GBP",
                    description=request.user.email,
                    source=request.POST["stripeToken"]
                )
            except stripe.error.CardError:
                messages.error(request, "Sorry, But your card was declined!")

            if customer.paid:
                feature_form.instance.user = request.user
                feature_form.instance.ticket_type_id = 2
                feature_form.instance.total_donations = donation_amount
                current_user_donated = Profile.objects.values_list(
                    "total_donated", flat=True).get(user_id=request.user.id)
                
                new_user_donated = current_user_donated + donation_amount
                # Push the new amount to the user's total donated amount
                Profile.objects.filter(user_id=request.user.id).update(
                    total_donated=new_user_donated)
                # The ticket's status will be 'working on' if user donates
                # the goal amount for the feature to be implemented
                if donation_amount >= int(200):
                    feature_form.instance.ticket_status_id = [2]
                else:
                    # If goal amount is not reached, ticket status will be Open
                    feature_form.instance.ticket_status_id = [1]
                feature_form.save()
                messages.success(request, f"Thanks for submitting a Feature Request!")
                return redirect(get_tickets)
            else:
                messages.error(request, "Unable to take payment")
        # If donation_form is not valid
        else:
            messages.error(request, f"We were unable to take a payment with that card. Please try again.")
    else:
        feature_form = FormForTickets()
        donation_form = DonationFormForTickets()

    args = {
        "feature_form": feature_form,
        "donation_form": donation_form,
        "publishable": settings.STRIPE_PUBLISHABLE
    }

    return render(request, "new_feature.html", args)


def view_one_ticket(request, pk):
    '''the user can view the details of selected ticket, it
    returns the selected ticket based on its ticket ID (pk) and renders it to the single_ticket.html template, or returns 404 error if object isn't found'''
    # Gets the details of the ticket
    ticket = get_object_or_404(TicketModel, pk=pk)
    # Options for the ticket status dropdown
    ticket_status_dropdown = TicketStatus.objects.all()
    ticket_status = ticket.ticket_status_id

    # Increases views by 1 when ticket is viewed
    ticket.views += 1
    ticket.save()

    # user's upvotes will be filtered by their user_id
    ticket_upvotes = Upvote.objects.filter(ticket_id=ticket.pk)\
        .values("user_id")
    user_upvotes = [upvote["user_id"] for upvote in ticket_upvotes]

    # Allows injection of donation form into Upvote & donate
    donation_form = DonationFormForTickets()

    comments = UserComments.objects.filter(ticket_id=ticket.pk)

    if request.method == "POST":
        comment_form = CommentFormForTickets(request.POST)
        # Save form and redirect user to the page for that ticket
        if comment_form.is_valid():
            comment_form.instance.user = request.user
            comment_form.instance.ticket = ticket
            comment_form.save()
            # Decrease views by -2
            ticket.views -= 2
            ticket.save()
            messages.success(
                request, f"Thankyou, Your comment has been added to this thread!")
            return redirect(view_one_ticket, ticket.pk)
    else:
        comment_form = CommentFormForTickets()

    args = {
        "ticket": ticket,
        
        "ticket_status": ticket_status,
        "ticket_status_dropdown": ticket_status_dropdown,
    
        "comment_form": comment_form,
        "comments": comments,
        "donation_form": donation_form,
        "publishable": settings.STRIPE_PUBLISHABLE,
        "user_upvotes": user_upvotes,

    }

    return render(request, "view_one_ticket.html", args)


@login_required
def upvote(request, pk):
    '''users can upvote a ticket but they must make a donation first to upvote a feature ticket'''
    ticket = get_object_or_404(TicketModel, pk=pk)

    # Increase the ticket's upvotes by 1 and decrease views by 1
    ticket.upvotes += 1
    ticket.views -= 1
    ticket.save()

    # If upvote is on a feature request, then a payment will be needed
    if request.method == "POST":
        donation_form = DonationFormForTickets(request.POST)
        if donation_form.is_valid():
            # Total Donation Amount
            donation_amount = 0
            donation_amount += int(request.POST.get("donation_amount"))
            try:
                # Use stripe's inbuilt API to create a customer and charge
                customer = stripe.Charge.create(
                    amount=int(donation_amount * 200),
                    currency="GBP",
                    description=request.user.email,
                    source=request.POST["stripeToken"]
                )
            except stripe.error.CardError:
                # Display error message if card is declined
                messages.error(request, "Ooops...Sorry, Your card was declined!")

            # If payment is successful
            if customer.paid:
                '''Create an object of the Upvote model to store the user's
                ID against the ticket - enables the user's upvote to
                be received if the user downvotes the ticket'''
                Upvote.objects.create(ticket_id=ticket.pk,
                                      user_id=request.user.id)

                # Add the donation to the user's total donated amount
                current_user_donated = Profile.objects.values_list(
                    "total_donated", flat=True).get(user_id=request.user.id)
                # Add new amount to the donation amount
                new_user_donated = current_user_donated + donation_amount
                # new amount is added to the user's total donated amount
                Profile.objects.filter(user_id=request.user.id).update(
                    total_donated=new_user_donated)

                # the donation is added to the ticket's total donations amount and view current total
                current_ticket_donations = TicketModel.objects.values_list(
                    "total_donations", flat=True).get(id=ticket.pk)
                # Add it to the donation amount
                new_ticket_donations = current_ticket_donations\
                    + donation_amount
                #  Add new amount to the ticket's total amount
                TicketModel.objects.filter(id=ticket.pk).update(
                    total_donations=new_ticket_donations)

                # Update the ticket's status to Working on if user donates the goal amount for the feature to be implemented
                if new_ticket_donations >= int(100):
                    TicketModel.objects.filter(id=ticket.pk).update(ticket_status_id=2)
                messages.success(
                    request, f"Thankyou, your payment has been approved and your upvote has been registered on this Ticket!")
                return redirect(view_one_ticket, ticket.pk)
            else:
                messages.error(
                    request, "Ooops..Sorry, Unable to take payment at this time")
        # If feature form or the donation form are not valid
        else:
            messages.error(
                request, f"Ooops, We were unable to take a payment with that card. Please try again.")
    else:
        '''Create an object of the Upvote model to store the user's
        ID against the ticket'''
        Upvote.objects.create(ticket_id=ticket.pk,
                              user_id=request.user.id)

        messages.success(
            request, f"Thankyou, your upvote has been registered on this Ticket!")

    return redirect(view_one_ticket, ticket.pk)


@login_required
def edit_ticket(request, pk):
    '''
    Allows users to edit a ticket, only if they have added it
    Inserts the current date in the edited_date field
    '''
    ticket = get_object_or_404(TicketModel, pk=pk)

    if request.method == "POST":
        edit_form = FormForTickets(request.POST, instance=ticket)
        # Save the form and redirect user to the page for that ticket
        if edit_form.is_valid():
            # Insert current date in the edited date field
            edit_form.instance.edited_date = timezone.now()
            edit_form.save()
            # Decrement views by -1 to prevent incorrect as it was updated not viewed
            ticket.views -= 1
            ticket.save()
            messages.success(request, f"Your ticket has successfully been \
                             edited!")
            return redirect(view_one_ticket, ticket.pk)
    else:
        # generate existing ticket data in the ticket_form
        edit_form = FormForTickets(instance=ticket)

    args = {
        "ticket": ticket,
        "edit_form": edit_form
    }

    return render(request, "edit_tickets.html", args)


@login_required
def delete_ticket(request, pk):
    """ User can delete their own ticket only """
    ticket = get_object_or_404(TicketModel, pk=pk)
    ticket.delete()
    messages.success(request, f"You have successfully deleted your ticket from Unicorn Attractor")
    return redirect(get_tickets)
