from django.conf.urls import url
from .views import (get_tickets, new_bug_ticket)

urlpatterns = [
    url(r'^$', get_tickets, name="get_tickets"),
    url(r'^new/bug$', new_bug_ticket, name="new_bug_ticket")
]
