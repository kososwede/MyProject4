from django.conf.urls import url, include
from accounts.views import logout, login, registration, user_profile, about
from accounts import url_reset


urlpatterns = [
    url(r'^register/$', registration, name='registration'),
    url(r'^profile/$', user_profile, name='profile'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^login/$', login, name='login'),
    url(r'^about/$', about, name='about'),
    url(r'^password-reset/', include(url_reset)),
]
