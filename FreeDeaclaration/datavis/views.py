from django.shortcuts import render
from .models import Region


def get_detail_stats(request):
    return render(request, 'data/integral_stat.html', {})


def get_base(request):
    return render(request, 'data/base.html', {})


def get_pl_map(request):
    return render(request, 'data/index.html', {})


def get_map(request):
    obj = Region.objects.get(id=11)
    return render(request, 'data/data.html', {'obj': obj})




