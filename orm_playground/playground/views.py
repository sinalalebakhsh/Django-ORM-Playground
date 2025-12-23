from django.shortcuts import render
from django.db.models import F
# Create your views here.
from decimal import Decimal, ROUND_HALF_UP

from playground.models.product import Product





def run_product_url(request):
    """
    # You have to solve it manually.
    for product in products:
        product.price = product.price * Decimal("1.1")
        product.save()
    
    # You have to solve it manually.
    for product in products:
        product.price = (product.price * Decimal("1.1")).quantize(
            Decimal("0.01"),
            rounding=ROUND_HALF_UP
        )
        product.save()

    Product.objects.update(price=F("price") * 1.1)    
    products = Product.objects.filter(category__name="Electronics")
    """
    
    """
        This line:
            Runs immediately
            Has no loops
            Has no save()
            Has no Decimal / float errors
    """
    Product.objects.filter(category__name="Electronics").update(price=F("price") * 1.1)
    Product.objects.filter(category__name="Electronics").values("name", "price")

    return render(request, 'sina.html')