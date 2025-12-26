from django.db import models

class OrderItem(models.Model):
    order = models.ForeignKey(
        'playground.Order',
        on_delete=models.CASCADE,
        related_name='items'
    )
    product = models.ForeignKey(
        'playground.Product',
        on_delete=models.CASCADE
    )
    quantity = models.IntegerField()



