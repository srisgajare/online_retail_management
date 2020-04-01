from django.contrib import admin

# Register your models here.

from ShoppersPoint.models import Category, Products, Mobiles, Laptops

admin.site.register(Category)

admin.site.register(Products)

admin.site.register(Mobiles)

admin.site.register(Laptops)

