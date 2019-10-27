from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView, ListAPIView
from datavis.models import Region
from .serializers import RegionSerializator


class RegionAPIView(RetrieveAPIView):
    serializer_class = RegionSerializator
    queryset = Region.objects.all()


class RegionList(ListAPIView):
    serializer_class = RegionSerializator

    def get_queryset(self):
        queryset = Region.objects.all()
        return queryset