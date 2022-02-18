from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_all_supers), 
    path('', views.make_super),
    path('<int:pk>/', views.get_supers_id)
]