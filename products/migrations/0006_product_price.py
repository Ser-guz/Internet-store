# Generated by Django 3.0.3 on 2020-03-12 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20200312_0528'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='Цена'),
        ),
    ]
