from django.contrib import admin
from .models import TicketType, TicketStatus, Ticket, Comments, Upvote
# Register your models here.


admin.site.register(TicketType)
admin.site.register(TicketStatus)
admin.site.register(Ticket)
admin.site.register(Comments)
admin.site.register(Upvote)
