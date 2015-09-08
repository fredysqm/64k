from django.conf.urls import patterns, include, url

from app.views import *

urlpatterns = patterns('',
    url(r'^$', slink_crear_view.as_view(), name='slink_crear_url'),
    url(r'^ver/(?P<slug>[-_\w]+)/$', slink_ver_view.as_view(), name='slink_ver_url'),
)