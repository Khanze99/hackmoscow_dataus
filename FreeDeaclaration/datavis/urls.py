from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_base, name='base'),
    path('dashboard/', views.get_map, name='interactive'),
    path('analyse/', views.get_pl_map, name='analyse'),
    path('statistics/', views.get_detail_stats, name='statistics'),
    path('budget/', views.get_budget_official, name='budget')
]
