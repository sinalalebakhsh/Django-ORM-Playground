from django.db import models
from .category import Category

class Product(models.Model):
    name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    category = models.ForeignKey('playground.Category',on_delete=models.CASCADE,related_name='products')

    def __str__(self):
        return self.name
