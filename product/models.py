from django.db import models

class Provider(models.Model):
    name            = models.CharField(max_length = 256)
    business_number = models.IntegerField(unique = True)
    phone_number    = models.CharField(max_length = 64)

class Product(models.Model):
    name        = models.CharField(max_length = 256, unique = True)
    price       = models.IntegerField()
    stock       = models.IntegerField()
    provider_id = models.ForeignKey(Provider, on_delete = models.CASCADE)
