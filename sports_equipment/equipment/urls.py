from django.urls import path
from . import views

urlpatterns = [
    path('', views.equipment_list, name='equipment_list'),
    path('add/', views.equipment_add, name='equipment_add'),
    path('edit/<int:pk>/', views.equipment_edit, name='equipment_edit'),
    path('delete/<int:pk>/', views.equipment_delete, name='equipment_delete'),
]
