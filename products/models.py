from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(
        u"Категория", max_length=128, blank=True, null=True, default=None)
    is_active = models.BooleanField(u"Активный", default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория товара'
        verbose_name_plural = 'Категории товаров'


class Product(models.Model):
    name = models.CharField(
        u"Имя", max_length=128, blank=True, null=True, default=None)
    category = models.ForeignKey(
        ProductCategory, on_delete=models.CASCADE, verbose_name='Категория', default=None, null=True, blank=True)
    price = models.DecimalField(
        u"Цена", max_digits=5, decimal_places=2, default=0)
    discount = models.IntegerField(u"Скидка", default=0)
    short_description = models.TextField(
        u"Описание (кратко)", max_length=100, blank=True, null=True, default=None)
    description = models.TextField(
        u"Описание", max_length=500, blank=True, null=True, default=None)
    created = models.DateTimeField(
        u"Создан", auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(
        u"Обновлён", auto_now_add=False, auto_now=True)
    is_active = models.BooleanField(u"Видимость", default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, verbose_name='Товар')
    image = models.ImageField(u"Путь", upload_to='products_images/')
    created = models.DateTimeField(
        u"Создан", auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(
        u"Обновлён", auto_now_add=False, auto_now=True)
    is_active = models.BooleanField(u"Видимость", default=True)
    is_main = models.BooleanField(u"На карточку", default=False)

    def __str__(self):
        return "Фото №%s товара %s" % (self.id, self.product.name)

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фотографии'
