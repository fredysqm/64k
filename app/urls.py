from django.conf.urls import url
from app.views import *


urlpatterns = [
    url(r'^$', slink_crear_view.as_view(), name='slink_crear_url'),    
    #url(r'^error404/$', error404.as_view()),
    #url(r'^error500/$', error500.as_view()),
    url(r'^ver/(?P<slug>[-_\w]+)/$', slink_ver_view.as_view(), name='slink_ver_url'),
    url(r'^(?P<slug>[-_\w]+)/$', slink_redirect_view.as_view(), name='slink_redirect_url'),
]