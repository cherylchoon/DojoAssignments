from django.conf.urls import url, include
from views import *

urlpatterns = [
    url(r'^$', index),
    url(r'^ninjas$', ninjas),
    url(r'^ninjas/(?P<ninja_color>\D+)$', ninja_color)
]
