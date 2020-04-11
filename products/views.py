from .models import *
from django.views.generic import DetailView


# Сделать ProductDetail на основе DetailView
class ProductDetail(DetailView):
    model = Product
    template_name = 'products/product.html'


# def product_view(request, product_id):
#     product = Product.objects.get(id=product_id)
#
#     session_key = request.session.session_key
#     if not session_key:
#         request.session.cycle_key()
#
#     print(request.session.session_key)
#
#     return render(request, 'products/product.html', {"product": product})
