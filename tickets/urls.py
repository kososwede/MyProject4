from django.conf.urls import url
from .views import (get_tickets)

urlpatterns = [
    url(r'^$', get_tickets, name="get_tickets"),
]
