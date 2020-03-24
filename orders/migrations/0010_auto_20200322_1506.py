# Generated by Django 3.0.3 on 2020-03-22 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_auto_20200320_1855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='price_total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Полная цена'),
        ),
        migrations.AlterField(
            model_name='productinbasket',
            name='price_per_item',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Цена товара'),
        ),
        migrations.AlterField(
            model_name='productinbasket',
            name='price_total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Полная цена'),
        ),
        migrations.AlterField(
            model_name='productinorder',
            name='price_per_item',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Цена товара'),
        ),
        migrations.AlterField(
            model_name='productinorder',
            name='price_total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Полная цена'),
        ),
    ]
