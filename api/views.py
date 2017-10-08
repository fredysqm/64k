from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import mixins
from app.models import Slink
from api.serializers import SlinkSerializer


class SlinkViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = SlinkSerializer
    queryset = Slink.objects.all()
    lookup_field = 'slug'
    
    def list(self, request):
        query = self.request.query_params
        if 'url' in query.keys():
            try:
                slink = Slink.objects.get(url=query.get('url'))
            except Slink.DoesNotExist:
                raise Http404
            
            serializer = SlinkSerializer(slink)
            return Response(serializer.data)
        else:
            raise Http404
