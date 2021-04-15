def cart_total_amount(request):
    total = 1000
    if request.user.is_authenticated:
        for key, value in request.session['cart'].items():
            total = total + (float(value['prince']) * value['quantity'])
    return {'cart_total_amount': total}