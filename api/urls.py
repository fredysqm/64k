from django.conf.urls import url

from api.views import *



urlpatterns = [
    url(r'^slink/$', SlinkAPIView.as_view()),
    url(r'^slink/(?P<slug>[-_\w]+)/$', SlinkDetailAPIView.as_view()),
]