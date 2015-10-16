from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^sp10ndmnumbr30n/', include(admin.site.urls)),
    url(r'^', include('app.urls')),
]
