from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter

from api.views import *



router = DefaultRouter()
router.register(r'slink2', SlinkViewSet)
router.register(r'slink2-search', SlinkListViewSet)


urlpatterns = [
    url(r'^slink/$', SlinkAPIView.as_view()),
    url(r'^slink/(?P<slug>[-_\w]+)/$', SlinkDetailAPIView.as_view()),
    url(r'^', include(router.urls)),
]