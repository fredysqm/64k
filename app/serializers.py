from app.models import Slink
from rest_framework import serializers


class SlinkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Slink