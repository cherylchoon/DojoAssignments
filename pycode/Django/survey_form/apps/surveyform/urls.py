from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^$', index),
    url(r'^survey_process$', survey_process),
    url(r'^result$', result)
]
