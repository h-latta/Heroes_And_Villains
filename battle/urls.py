from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_battle), 
    path('<int:pk>/', views.get_battle_id)
]