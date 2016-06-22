from django.http import Http404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from app.models import Slink

from api.serializers import SlinkSerializer



class SlinkAPIView(APIView):

    def post(self, request, format=None):
        serializer = SlinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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