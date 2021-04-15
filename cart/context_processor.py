def cart_total_amount(request):
    total = 0.0
    if request.user.is_authenticated:
        for key, value in request.session['cart'].items():
            total = total + (float(value['price']))
    return {'cart_total_amount': total}