from django.shortcuts import render
from products.models import *
from django.views.decorators.csrf import csrf_protect


@csrf_protect
def ProductView(request, product_id):
    product = Product.objects.get(id=product_id)

    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()

    print(request.session.session_key)

    return render(request, 'products/product.html', locals())
