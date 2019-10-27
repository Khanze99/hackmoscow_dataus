from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_map, name='image'),
    path('api/', views.API.as_view(), name='api'),
    path('api/obj/<int:pk>/', views.RegionAPIView.as_view(), name='obj'),
    path('api/list/', views.RegionList.as_view(), name='list')]
