from django.db import models
from products.models import Product
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Status(models.Model):
    name = models.CharField(u"Имя", max_length=56, blank=True, null=True, default=None)
    is_active = models.BooleanField(u"Видимость", default=True)
    created = models.DateTimeField(u"Создан", auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(u"Обновлён", auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


class Order(models.Model):
    user = models.ForeignKey(User, verbose_name='Клиент', blank=True, null=True, default=None, on_delete=models.CASCADE,)
    customer_name = models.CharField(u"Имя покупателя", max_length=128, blank=True, null=True, default=None)
    customer_email = models.EmailField(u"Email покупателя")
    customer_phone = models.CharField(u"Телефон покупателя", max_length=32, blank=True, null=True, default=None)
    comments = models.TextField(u"Комментарий", max_length=256, blank=True, null=True, default=None)
    price_total = models.DecimalField(u"Полная цена", max_digits=10, decimal_places=2, default=0)
    created = models.DateTimeField(u"Создан", auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(u"Обновлён", auto_now_add=False, auto_now=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, verbose_name='Статус')
    is_active = models.BooleanField(u"Видимость", default=True)

    def __str__(self):
        return "Заказ №%s, статус: %s." % (self.id, self.status.name)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class ProductInOrder(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар')
    amount = models.IntegerField(u"Количество товаров", default=1)
    price_per_item = models.DecimalField(u"Цена товара", max_digits=10, decimal_places=2, default=0)
    price_total = models.DecimalField(u"Полная цена", max_digits=10, decimal_places=2, default=0)
    created = models.DateTimeField(u"Создан", auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(u"Обновлён", auto_now_add=False, auto_now=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Заказ')
    is_active = models.BooleanField(u"Видимость", default=True)

    def __str__(self):
        return self.product.name

    class Meta:
        verbose_name = 'Товар в заказе'
        verbose_name_plural = 'Товары в заказе'

    def save(self, *args, **kwargs):
        price_per_item = self.product.price
        self.price_per_item = price_per_item
        self.price_total = int(self.amount) * price_per_item

        super(ProductInOrder, self).save(*args, **kwargs)


def product_in_order_post_save(sender, instance, created, **kwargs):
    order = instance.order
    all_product_in_order = ProductInOrder.objects.filter(
        order=order, is_active=True)

    order_price_total = 0
    for item in all_product_in_order:
        order_price_total += item.price_total

    instance.order.price_total = order_price_total
    instance.order.save(force_update=True)


post_save.connect(product_in_order_post_save, sender=ProductInOrder)


class ProductInBasket(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар')
    amount = models.IntegerField(u"Количество товаров", default=1)
    price_per_item = models.DecimalField(u"Цена товара", max_digits=10, decimal_places=2, default=0)
    price_total = models.DecimalField(u"Полная цена", max_digits=10, decimal_places=2, default=0)
    created = models.DateTimeField(u"Создан", auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(u"Обновлён", auto_now_add=False, auto_now=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Заказ', blank=True,
                              null=True, default=None)
    is_active = models.BooleanField(u"Видимость", default=True)
    session_key = models.CharField(max_length=128, default=0)

    def __str__(self):
        return self.product.name

    class Meta:
        verbose_name = 'Товар в корзине'
        verbose_name_plural = 'Товары в корзине'

    def save(self, *args, **kwargs):
        price_per_item = self.product.price
        self.price_per_item = price_per_item
        self.price_total = int(self.amount) * price_per_item

        super(ProductInBasket, self).save(*args, **kwargs)
