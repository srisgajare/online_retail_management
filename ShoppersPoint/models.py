from django.db import models


# Create your models here.


class Category(models.Model):
    category_type = models.CharField(max_length=250, primary_key=True)
    category_info = models.CharField(max_length=1000, default='')

    def __str__(self):
        return self.category_type

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Products(models.Model):
    product_id = models.IntegerField(primary_key=True)
    product_name = models.CharField(max_length=1000, default='')
    stock = models.IntegerField(default=0)
    price = models.FloatField(default=0)
    discounted_price = models.FloatField(default=0)
    category_type = models.ForeignKey(Category, on_delete=models.CASCADE)
    image_src = models.CharField(max_length=2000, default='')

    def __str__(self):
        return str(self.product_id) + ' -- ' + self.product_name

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"


class Mobiles(models.Model):
    product_id = models.ForeignKey(Products, primary_key=True, on_delete=models.CASCADE)
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    model_name = models.CharField(max_length=1000, default='')
    color = models.CharField(max_length=250, default='')
    display_size = models.CharField(max_length=100, default='')
    resolution = models.CharField(max_length=100, default='')
    ram = models.CharField(max_length=100, default='')
    storage = models.CharField(max_length=100, default='')
    primary_camera = models.CharField(max_length=250, default='')
    secondary_camera = models.CharField(max_length=250, default='')
    warranty_summary = models.CharField(max_length=2000, default='')

    def __str__(self):
        return self.product_id.product_name

    class Meta:
        verbose_name = "Mobile"
        verbose_name_plural = "Mobiles"


class Laptops(models.Model):
    product_id = models.ForeignKey(Products, primary_key=True, on_delete=models.CASCADE)
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_content = models.CharField(max_length=1000, default='')
    color = models.CharField(max_length=250, default='')
    brand = models.CharField(max_length=100, default='')
    processor = models.CharField(max_length=100, default='')
    ram = models.CharField(max_length=100, default='')
    ram_type = models.CharField(max_length=100, default='')
    storage = models.CharField(max_length=250, default='')
    display = models.CharField(max_length=250, default='')
    warranty_summary = models.CharField(max_length=2000, default='')

    def __str__(self):
        return self.product_id.product_name

    class Meta:
        verbose_name = "Laptop"
        verbose_name_plural = "Laptops"
