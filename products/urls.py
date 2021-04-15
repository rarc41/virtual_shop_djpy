from django.urls import path
from .views import listado_productos


urlpatters = [
    path('', listado_productos, name='listado_productos')
]