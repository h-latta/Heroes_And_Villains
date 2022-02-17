from django.urls import path
from django import views
from . import views

urlpatterns = [
    path('', views.get_all_supers, views.make_super),
    path('<int:pk>/', views.get_supers_id),
]