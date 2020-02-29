from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class TypeOfTicket(models.Model):
    """ Choose ticket type (bug or feature)"""
    TICKET_TYPE_CHOICE = (("Bug", "Bug"), ("Feature", "Feature"))
    TicketType = models.CharField(
        max_length=7,
        unique=True,
        choices=TICKET_TYPE_CHOICE)

    def __str__(self):
        return self.TicketType


class StatusOfTicket(models.Model):
    """status of ticket open, working on or closed"""
    STATUS_CHOICE = (("Open", "Open"), ("Working on", "Working on"), ("Closed", "Closed"))
    TicketStatus = models.CharField(
        max_length=10,
        unique=True,
        choices=STATUS_CHOICE)

    def __str__(self):
        return self.TicketStatus


class Tickets(models.Model):
    '''Allows users to log bug/feature tickets'''
    user = models.ForeignKey(
        User,
        null=True,
        on_delete=models.CASCADE)
    created_date = models.DateTimeField(
        blank=False,
        null=False,
        auto_now_add=True)
    TicketType = models.ForeignKey(
        TypeOfTicket,
        null=True)
    TicketStatus = models.ForeignKey(
        StatusOfTicket,
        null=True)
    title = models.CharField(
        max_length=80,
        blank=False)
    description = models.TextField(
        max_length=1500,
        blank=False)
    views = models.IntegerField(
        default=0)
    upvotes = models.IntegerField(
        default=0)
    edited_date = models.DateTimeField(
        blank=False,
        null=False,
        default=timezone.now)
    total_donations = models.IntegerField(
        default=0)

    class Meta:
        ordering = ("-upvotes", )

    def __str__(self):
        return "#{0} [{1} - {2}] - {3}".format(
            self.id, self.TicketType, self.TicketStatus, self.title)


class Comments(models.Model):
    '''user to comment on tickets'''

    comment_date = models.DateTimeField(
        auto_now_add=True)
    ticket = models.ForeignKey(
        Tickets,
        null=True,
        on_delete=models.CASCADE)
    user = models.ForeignKey(
        User,
        null=True,
        on_delete=models.CASCADE)
    description = models.TextField(
        max_length=1500,
        blank=False,
        null=True)

    def __str__(self):
        return "Comment by {0} on Ticket #{1}".format(
            self.user.username, self.ticket.id)


class Upvote(models.Model):
    '''users can upvote any ticket'''
    ticket = models.ForeignKey(
        Tickets,
        null=True,
        on_delete=models.CASCADE)
    user = models.ForeignKey(
        User,
        null=True,
        on_delete=models.CASCADE)

    def __str__(self):
        return "Upvoted by {0} on Ticket #{1}".format(
            self.user.username, self.ticket.id)
