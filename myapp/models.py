from django.db import models
# from django.models import User
# Create your models here.


class Product(models.Model):
    product_id = models.AutoField
    product_name=models.CharField(max_length=60)
    product_price=models.IntegerField(default=0)
    product_description = models.CharField(max_length=1000,default="")
    # product_image = models.ImageField()
    category = models.CharField(max_length=60,default="")
    image = models.ImageField(upload_to = 'static/img/man', default = "")

    def __str__(self):
        return self.product_name