from django.conf.urls import url
from .views import (get_tickets, new_bug_ticket, new_feature_ticket,
                    view_one_ticket, upvote, downvote,
                    admin_update_status, edit_ticket, delete_ticket)

urlpatterns = [
    url(r"^$", get_tickets, name="get_tickets"),
    url(r"^new/bug$", new_bug_ticket, name="new_bug_ticket"),
    url(r"^new/feature$", new_feature_ticket, name="new_feature_ticket"),
    url(r"^(?P<pk>\d+)$", view_one_ticket, name="view_one_ticket"),
    url(r"^edit/(?P<pk>\d+)$", edit_ticket, name="edit_ticket"),
    url(r"^delete/(?P<pk>\d+)$", delete_ticket, name="delete_ticket"),
    url(r"^upvote/(?P<pk>\d+)$", upvote, name="upvote"),
    url(r"^downvote/(?P<pk>\d+)$", downvote, name="downvote"),
    url(r"^admin/update-status/(?P<pk>\d+)$", admin_update_status,
        name="admin_update_status"),
]
