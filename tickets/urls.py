from django.conf.urls import url
from .views import (get_tickets, new_bug, new_feature,
                    view_one_ticket, upvote, edit_ticket, delete_ticket)

urlpatterns = [
    url(r"^$", get_tickets, name="get_tickets"),
    url(r"^new/bug$", new_bug, name="new_bug_ticket"),
    url(r"^new/feature", new_feature, name="new_feature_ticket"),
    url(r"^(?P<pk>\d+)$", view_one_ticket, name="view_one_ticket"),
    url(r"^edit/(?P<pk>\d+)$", edit_ticket, name="edit_ticket"),
    url(r"^delete/(?P<pk>\d+)$", delete_ticket, name="delete_ticket"),
    url(r"^upvote/(?P<pk>\d+)$", upvote, name="upvote"),

]
