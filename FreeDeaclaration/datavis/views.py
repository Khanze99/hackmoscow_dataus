from django.shortcuts import render
from django.core.files import File
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.response import Response
from .serializers import RegionSerializator
from django.conf import settings
from requests import get, post
from .models import Region
import json


# Create your views here.
# def get_image(request):
#

def get_pl_map(request):
    return render(request, 'data/index.html', {})


def get_map(request):
    obj = Region.objects.get(id=11)
    return render(request, 'data/data.html', {'obj': obj})


class API(APIView):
    def get(self, request):
        data = self.request.query_params
        obj = Region.objects.get(id=5)
        return Response({'region': obj.region})


class RegionAPIView(RetrieveAPIView):
    serializer_class = RegionSerializator
    queryset = Region.objects.all()


class RegionList(ListAPIView):
    serializer_class = RegionSerializator

    def get_queryset(self):
        queryset = Region.objects.all()
        return queryset

