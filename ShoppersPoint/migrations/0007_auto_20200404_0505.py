# Generated by Django 3.0.4 on 2020-04-04 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShoppersPoint', '0006_remove_laptops_ssd'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='laptops',
            name='image_src',
        ),
        migrations.RemoveField(
            model_name='mobiles',
            name='image_src',
        ),
        migrations.AddField(
            model_name='products',
            name='image_src',
            field=models.CharField(default='', max_length=2000),
        ),
    ]
