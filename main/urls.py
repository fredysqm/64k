from django.urls import path, include
from django.contrib import admin
from app.views import error404, error500
from django.conf import settings

urlpatterns = [
    path( 'adminplus/', admin.site.urls ),
    path( 'api/', include('api.urls') ),
    path( '', include('app.urls') ),
]
#handler404 = error404.as_view()
#handler500 = error500.as_view()

if settings.DEBUG:
    from django.conf.urls import url
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns