from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='blog'),
    path('post/crear', crear_post, name='crear_post'),
    path('post/eliminar/<int:post_id>', eliminar_post, name='eliminar_post'),

]
