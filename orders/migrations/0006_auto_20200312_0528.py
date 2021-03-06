# Generated by Django 3.0.3 on 2020-03-12 02:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20200312_0528'),
        ('orders', '0005_auto_20200312_0526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productinorder',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Order', verbose_name='Заказ'),
        ),
        migrations.AlterField(
            model_name='productinorder',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product', verbose_name='Товар'),
        ),
    ]
