from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello, name='hello'),
    path('api/', views.API.as_view(), name='api')
]
