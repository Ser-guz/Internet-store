from .models import ProductInBasket

# Из контексного процессора передаем в темплейт переменные.


def getting_basket_info(request):
    session_key = request.session.session_key
    # Если нет session_key, то создать его
    if not session_key:
        request.session.cycle_key()

    products_in_basket = ProductInBasket.objects.filter(
        session_key=session_key, is_active=True)
    products_total_amount = products_in_basket.count()

    return locals()
