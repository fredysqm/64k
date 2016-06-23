from django.conf import settings
from django.core import validators

from rest_framework import serializers

from app.models import Slink



SLINK_DOMAIN = getattr(settings, 'SLINK_DOMAIN')


class SlinkSerializer(serializers.ModelSerializer):

    class Meta:
        model = Slink
        fields = ('url', 'slug',)

    def validate_slug(self, value):
        if len(value) > 16:
            raise serializers.ValidationError('Slug no es válido.')
        return value

    def validate_url(self, value):
        if SLINK_DOMAIN in value:
            raise serializers.ValidationError('Url no es válida.')
        return value