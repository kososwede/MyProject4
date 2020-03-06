from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class TypeTicket(models.Model):
    """ Choose ticket type (bug or feature)"""
    TICKET_CHOICE_TYPE = (
        ("Bug", "Bug"),
        ("Feature", "Feature"),
    )
    ticket_type = models.CharField(
        max_length=7,
        unique=True,
        choices=TICKET_CHOICE_TYPE
    )

    def __str__(self):
        return self.ticket_type


class StatusTicket(models.Model):
    """status of ticket open, working on or closed"""
    TICKET_CHOICE_STATUS = [
        ('Open', "Open"),
        ('In Progress', "In Progress"),
        ('Closed', "Closed"),
    ]
    ticket_status = models.CharField(
        max_length=10,
        unique=True,
        choices=TICKET_CHOICE_STATUS
    )

    def __str__(self):
        return self.ticket_status


class Ticket(models.Model):
    '''Allows users to log bug/feature tickets'''
    user = models.ForeignKey(
        User,
        null=True,
        on_delete=models.CASCADE)
    created_date = models.DateTimeField(
        blank=False,
        null=False,
        auto_now_add=True)
    ticket_type = models.ForeignKey(
        TypeTicket,
        null=True)
    ticket_status = models.ForeignKey(
        StatusTicket,
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
            self.id, self.ticket_type, self.ticket_status, self.title)


class Comments(models.Model):
    '''user to comment on tickets'''

    comment_date = models.DateTimeField(
        auto_now_add=True)
    ticket = models.ForeignKey(
        Ticket,
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
        Ticket,
        null=True,
        on_delete=models.CASCADE)
    user = models.ForeignKey(
        User,
        null=True,
        on_delete=models.CASCADE)

    def __str__(self):
        return "Upvoted by {0} on Ticket #{1}".format(
            self.user.username, self.ticket.id)
