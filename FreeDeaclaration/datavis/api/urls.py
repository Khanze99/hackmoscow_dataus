from django.urls import path
from . import views

urlpatterns = [
    path('api/obj/<int:pk>/', views.RegionAPIView.as_view(), name='obj'),
    path('api/list/', views.RegionList.as_view(), name='list')]