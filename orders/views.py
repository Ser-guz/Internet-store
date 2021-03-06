from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from .forms import CheckoutContactForm
from django.contrib.auth.models import User
from django.views.generic import CreateView


def basket_adding(request):
    # Создание словаря
    return_dict = dict()

    session_key = request.session.session_key
    print(request.POST)
    data = request.POST
    product_id = data.get('product_id')
    amount = data.get('amount')
    is_delete = data.get("is_delete")

    if is_delete == "true":
        ProductInBasket.objects.filter(id=product_id).update(is_active=False)
    else:
        # get_or_created - если строка найдена в базе данных, то ничего не делать, если её нет,
        # то создает новую запись, используя первые 2 поля, 3 поле дается по умолчанию.
        new_product, created = ProductInBasket.objects.get_or_create(session_key=session_key,
                                                                     product_id=product_id,
                                                                     is_active=True,
                                                                     defaults={"amount": amount})
        if not created:
            new_product.amount += int(amount)
            new_product.save(force_update=True)

    products_total_amount = ProductInBasket.objects.filter(session_key=session_key,
                                                           is_active=True).count()
    # Назначение элементу словаря по индексу
    return_dict["products_total_amount"] = products_total_amount

    # Создание списка в качестве элемента словаря
    return_dict['products'] = list()

    products_in_basket = ProductInBasket.objects.filter(session_key=session_key,
                                                        is_active=True)

    # Цикл по элементам QuerySet'а, полученного из контент_процессора
    for item in products_in_basket:
        product_dict = dict()
        product_dict['id'] = item.id
        product_dict['name'] = item.product.name
        product_dict['price_per_item'] = item.price_per_item
        product_dict['amount'] = item.amount
        # Добавление в элемент словаря в качестве списка
        return_dict['products'].append(product_dict)

    return JsonResponse(return_dict)


def checkout(request):
    session_key = request.session.session_key
    products_in_basket = ProductInBasket.objects.filter(session_key=session_key, is_active=True)
    form = CheckoutContactForm(request.POST or None)

    if request.method == "POST":
        print(request.POST)
        if form.is_valid():
            print("Да, хорошо.")
            # Получение из базы данных покупателя или создание нового
            data = request.POST
            name = data.get("name")
            phone = data["phone"]
            user, created = User.objects.get_or_create(
                username=phone, defaults={"first_name": name})

            # Создание нового заказа
            order = Order.objects.create(user=user, customer_name=name, customer_phone=phone, status_id=1)
            for name, value in data.items():  # проход циклом по словарю с помощью двух аргументов и функции items()
                if name.startswith("product_in_basket_"):
                    product_in_basket_id = name.split("product_in_basket_")[1]
                    product_in_basket = ProductInBasket.objects.get(id=product_in_basket_id)
                    product_in_basket.amount = value
                    product_in_basket.order = order
                    product_in_basket.save(force_update=True)

                    # Создание продуктов в заказе с соответствующими свойствами
                    ProductInOrder.objects.create(product=product_in_basket.product,
                                                  amount=product_in_basket.amount,
                                                  price_per_item=product_in_basket.price_per_item,
                                                  price_total=product_in_basket.price_total,
                                                  order=order)
        else:
            print("Нет, не подходят контактные данные")

    context = {"form": form,
               "products_in_basket": products_in_basket}

    return render(request, 'orders/checkout.html', context)
