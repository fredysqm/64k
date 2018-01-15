from django.conf.urls import include, url
from django.contrib import admin
from app.views import error404, error500
from django.conf import settings


handler404 = error404.as_view()
handler500 = error500.as_view()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('api.urls')),
    url(r'^', include('app.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns