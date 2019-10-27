from rest_framework import serializers
from datavis.models import Region


class RegionSerializator(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ('id_region', 'region', 'lat', 'lon')
