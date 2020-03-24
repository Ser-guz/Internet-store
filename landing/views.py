from django.shortcuts import render
from django.http import HttpResponse
from .forms import SubscribersForm
from products.models import *


def LandingView(request):
    form = SubscribersForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        new_form = form.save()

    return render(request, 'landing/landing_page.html', locals())


def HomeView(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True)
    products_images_groats = products_images.filter(product__category__id=1)
    products_images_nuts = products_images.filter(product__category__id=2)
    products_images_flour = products_images.filter(product__category__id=3)
    return render(request, 'landing/home.html', locals())
