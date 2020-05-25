import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Product(models.Model):
    product_gtin = models.CharField(max_length=200,  primary_key=True)
    exp_date = models.DateTimeField('expiry date')
    def __str__(self):
        return self.product_gtin +","+ (self.exp_date).strftime('%Y-%m-%d')

