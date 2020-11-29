from django.db import models
from product.models import Product
from shipper.models import Shipper

class Customer(models.Model):
    name         = models.CharField(max_length = 64, null = False)
    phone_number = models.CharField(max_length = 64, unique = True, null = False)
    password     = models.CharField(max_length = 256, null = True)
    new_address  = models.CharField(max_length = 256, null = False)
    old_address  = models.CharField(max_length = 256, null = False)

class Order(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete = models.CASCADE)
    product_id  = models.ForeignKey(Product, on_delete = models.CASCADE)
    quantity    = models.IntegerField(null = False)
    address     = models.CharField(max_length = 256, default = '', null = False)
    shipper_id  = models.ForeignKey(Shipper, on_delete = models.CASCADE)
    status      = models.IntegerField(null = False)
