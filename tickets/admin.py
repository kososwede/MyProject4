from django.contrib import admin
from .models import TicketTypeModel, TicketStatusModel, TicketModel, CommentModel, UpvoteModel
# Register your models here.


admin.site.register(TicketTypeModel)
admin.site.register(TicketStatusModel)
admin.site.register(TicketModel)
admin.site.register(CommentModel)
admin.site.register(UpvoteModel)
