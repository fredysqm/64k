from django.http import Http404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import mixins

from app.models import Slink

from api.serializers import SlinkSerializer



class SlinkAPIView(APIView):

    def get_object(self, url):
        try:
            return Slink.objects.get(url=url)
        except Slink.DoesNotExist:
            raise Http404

    def post(self, request, format=None):
        serializer = SlinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        slug = self.get_object(request.GET['url'])
        serializer = SlinkSerializer(slug)
        return Response(serializer.data)


class SlinkDetailAPIView(APIView):

    def get_object(self, slug):
        try:
            return Slink.objects.get(slug=slug)
        except Slink.DoesNotExist:
            raise Http404

    def get(self, request, slug, format=None):
        slug = self.get_object(slug)
        serializer = SlinkSerializer(slug)
        return Response(serializer.data)


class SlinkViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):

    serializer_class = SlinkSerializer
    queryset = Slink.objects.all()
    lookup_field = 'slug'
    

class SlinkListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    
    serializer_class = SlinkSerializer
    queryset = Slink.objects.all()
    
    def get_queryset(self):
        query = self.request.query_params
        queryset = self.queryset
        if 'url' in query.keys():
            queryset = queryset.filter(url=query.get('url'))
        else:
            raise Http404
        return queryset