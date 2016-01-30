from django.conf.urls import include, url
from django.contrib import admin

from app.views import error404, error500



urlpatterns = [
    url(r'^sp10ndmnumbr30n/', include(admin.site.urls)),
    url(r'^', include('app.urls')),
]

handler404 = error404.as_view()
handler500 = error500.as_view()