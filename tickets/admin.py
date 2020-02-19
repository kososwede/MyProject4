from django.contrib import admin
from .models import TypeOfTicket, StatusOfTicket, Tickets, Comments, Upvote
# Register your models here.


admin.site.register(TypeOfTicket)
admin.site.register(StatusOfTicket)
admin.site.register(Tickets)
admin.site.register(Comments)
admin.site.register(Upvote)