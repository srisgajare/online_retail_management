# Generated by Django 3.0.4 on 2020-04-01 19:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ShoppersPoint', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='laptops',
            name='discounted_price',
        ),
        migrations.RemoveField(
            model_name='laptops',
            name='price',
        ),
        migrations.RemoveField(
            model_name='laptops',
            name='product_name',
        ),
        migrations.RemoveField(
            model_name='mobiles',
            name='discounted_price',
        ),
        migrations.RemoveField(
            model_name='mobiles',
            name='price',
        ),
        migrations.RemoveField(
            model_name='mobiles',
            name='product_name',
        ),
    ]
