from django.contrib import admin
from blog.models import Categoria, Post


admin.site.register([Categoria, Post])
