from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from .models import Product


# Create your views here.
@login_required(login_url='/autenticacion/acceder')
def listado_productos(request):
    cart = Cart(request)
    #cart.clear()
    products = Product.objects.all()
    return render(request, "products/listado.html", {
        "products": products
    })

