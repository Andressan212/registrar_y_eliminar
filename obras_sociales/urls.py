# obras_sociales/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_obras_sociales, name='listar_obras_sociales'),
    path('registrar/', views.registrar_obra_social, name='registrar_obra_social'),
    path('eliminar/<int:obra_id>/', views.eliminar_obra_social, name='eliminar_obra_social'),
]
