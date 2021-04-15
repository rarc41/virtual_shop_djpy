from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('autenticacion.urls')),
    path('admin/', admin.site.urls),
    path('autenticacion/', include('autenticacion.urls')),
    path('products/', include('products.urls')),
    path('cart/', include('cart.urls')),
    path('orders/', include('orders.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
