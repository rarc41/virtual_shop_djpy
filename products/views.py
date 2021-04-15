from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Product


# Create your views here.
@login_required(login_url='/autenticacion/acceder')
def listado_productos(request):
    products = Product.objects.all()
    return render(request, "products/listado.html", {
        "products": products
    })

