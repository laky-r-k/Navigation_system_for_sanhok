from django.urls import path
from . import views

urlpatterns = [
    path('find/', views.find_path, name='find_path'),
    path('', views.map_view, name='map')
]
