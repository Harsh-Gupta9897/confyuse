from django.db import models

# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=255,unique=True)
    category = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=2,max_digits=4)


    def __str__(self):
        return self.product_name