from django.urls import path
from gestion_fechas import views

urlpatterns = [
    path('inicio/', views.inicio),
    path('create/', views.create),
    path('c/', views.c),
    path('read/', views.leer),  
    path('l/', views.l),
    path('update/', views.actualizar), 
    path('a/', views.a), 
    path('delete/', views.eliminar),  
    path('e/', views.e), 
]
