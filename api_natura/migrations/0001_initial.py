# Generated by Django 4.1.7 on 2023-03-04 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('product_id', models.IntegerField(max_length=12, primary_key=True, serialize=False)),
                ('product_name', models.CharField(default='', max_length=60)),
                ('product_category', models.CharField(default='', max_length=60)),
                ('product_usage', models.CharField(default='', max_length=250)),
                ('product_description', models.CharField(default='', max_length=250)),
                ('product_longDescription', models.CharField(default='', max_length=250)),
                ('product_activeIngredient', models.CharField(default='', max_length=250)),
                ('product_quantity', models.IntegerField(default=0, max_length=9)),
                ('product_price', models.FloatField(default=0, max_length=9)),
                ('product_salesPrice', models.FloatField(default=0, max_length=9)),
            ],
        ),
    ]
