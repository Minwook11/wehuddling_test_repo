from django.db import models

class Shipper(models.Model):
    phone_number = models.CharField(max_length = 64, unique = True)
    region       = models.CharField(max_length = 128)
