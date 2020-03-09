from django.contrib import admin
from .models import TicketType, TicketStatus, Ticket, Comment, Upvote
# Register your models here.


admin.site.register(TicketType)
admin.site.register(TicketStatus)
admin.site.register(Ticket)
admin.site.register(Comment)
admin.site.register(Upvote)
