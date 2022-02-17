from django.urls import path
from django import views
from . import views

urlpatterns = [
    path('', views.get_all_supers),
    path('<int:pk>/', views.get_supers_id),
]