from django.contrib import admin
from .models import TypeTicket, StatusTicket, Ticket, Comments, Upvote
# Register your models here.


admin.site.register(TypeTicket)
admin.site.register(StatusTicket)
admin.site.register(Ticket)
admin.site.register(Comments)
admin.site.register(Upvote)
