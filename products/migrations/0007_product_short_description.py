# Generated by Django 3.0.3 on 2020-03-15 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='short_description',
            field=models.TextField(blank=True, default=None, max_length=100, null=True, verbose_name='Описание'),
        ),
    ]
