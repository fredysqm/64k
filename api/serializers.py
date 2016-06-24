from rest_framework import serializers

from app.models import Slink



class SlinkSerializer(serializers.ModelSerializer):

    class Meta:
        model = Slink
        fields = ('url', 'slug',)