from django.urls import path
from .views import *

urlpatterns = [
    path('registro/', VistaRegistro.as_view(), name='registro'),
    path('salir/', salir, name='salir'),
    path('acceder/', acceder, name='acceder'),
]
