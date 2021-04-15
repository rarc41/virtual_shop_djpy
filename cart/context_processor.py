def cart_total_amount(request):
    total = 0
    if request.user.is_authenticated:
        for key, value in request.session['cart'].items():
            total = total + (float(value['price']) * value['quantity'])
    return {'cart_total_amount': total}