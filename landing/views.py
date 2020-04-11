from django.shortcuts import render
from .forms import SubscribersForm
from django.views.generic import ListView, CreateView
from products.models import *
from .models import Subscriber


# Вьюшка создает новый экземпляр модели "Подписчик" по введеным в форму данным
class LandingCreateView (CreateView):
    model = Subscriber
    template_name = 'landing/landing_page.html'
    fields = []


# def landing_view(request):
#     form = SubscribersForm(request.POST or None)
#
#     if request.method == "POST" and form.is_valid():
#         new_form = form.save()
#
#     return render(request, 'landing/landing_page.html', {"form": form})


# def home_view(request):
#     products_images = ProductImage.objects.filter(is_active=True, is_main=True)
#     # is_main - это атрибут изображения, кот. позволяет изображению попасть на карточку товара на странице листинга
#     # Тут нет бага, значение этого атрибута вводится при загрузке изображения товара.
#
#     products_images_groats = products_images.filter(product__category__id=1)
#     products_images_nuts = products_images.filter(product__category__id=2)
#
#     context = {"products_images": products_images,
#                "products_images_groats": products_images_groats,
#                "products_images_nuts": products_images_nuts,
#                "products_images_flour": products_images_flour}
#
#     return render(request, 'landing/home.html', context)


class HomeListView (ListView):
    model = ProductImage

    # Переопределение пути к темплейту
    template_name = 'landing/home.html'
    # Создание дружественного контекста - изменение названия QuerySet'ad
    context_object_name = 'products_images'
    # Изменение набора объектов - создание для них фильтра
    queryset = ProductImage.objects.filter(is_active=True, is_main=True)

    # Добавление переменных с дополнительными QuerySet'ами
    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        context['products_images_groats'] = ProductImage.objects.filter(is_active=True,
                                                                       is_main=True,
                                                                       product__category__id=1)
        context['products_images_nuts'] = ProductImage.objects.filter(is_active=True,
                                                                     is_main=True,
                                                                     product__category__id=2)
        return context
