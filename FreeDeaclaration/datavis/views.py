from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.


def hello(request):
    return render(request, 'data/data.html', {})


class API(APIView):
    def get(self, request):
        return Response({'hello': 'FreeDeclaration'})
