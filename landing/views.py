from django.shortcuts import render
from django.http import HttpResponse
from .forms import SubscribersForm
from products.models import *


def landing_view(request):
    form = SubscribersForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        new_form = form.save()

    return render(request, 'landing/landing_page.html', {"form": form})


def home_view(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True)
    # is_main - это атрибут изображения, кот. позволяет изображению попасть на карточку товара на странице листинга
    # Тут нет бага, значение этого атрибута вводится при загрузке изображения товара.

    products_images_groats = products_images.filter(product__category__id=1)
    products_images_nuts = products_images.filter(product__category__id=2)
    products_images_flour = products_images.filter(product__category__id=3)
    return render(request, 'landing/home.html', {
        "products_images": products_images,
        "products_images_groats": products_images_groats,
        "products_images_nuts": products_images_nuts,
        "products_images_flour": products_images_flour
    })
