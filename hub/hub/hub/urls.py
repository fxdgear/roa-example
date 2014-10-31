from django.conf.urls import patterns, include, url
from django.contrib import admin

from profiles.api import LoginView

urlpatterns = patterns('',  # NOQA
    url(r'^admin/', include(admin.site.urls)),
    url(r'^users/login/$', LoginView.as_view(), name='users-login'),
)

from profiles.urls import urlpatterns as user_urls

urlpatterns += user_urls
