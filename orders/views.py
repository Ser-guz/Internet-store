from django.shortcuts import render
from django.http import JsonResponse
from .models import ProductInBasket


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

    # Костыль - это переменная должна была загрузиться из context_processors
    products_in_basket = ProductInBasket.objects.filter(
        session_key=session_key, is_active=True)

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
