# Generated by Django 4.1.7 on 2023-03-06 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_natura', '0005_remove_products_product_unitprice_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='product_longDescription',
            field=models.CharField(default='', max_length=500),
        ),
    ]
