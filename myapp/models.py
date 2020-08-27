from django.db import models

# Create your models here.

class Product(models.Model):
    product_id = models.AutoField
    product_name=models.CharField(max_length=60)
    product_price=models.IntegerField()
    product_description = models.CharField(max_length=1000)
    product_image = models.ImageField()

    def __init__(self):
        return self.product_name