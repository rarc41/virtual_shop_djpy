from django.urls import path
from .views import *


urlpatterns = [
    path('', listado_productos, name='listado_productos')
]