from django.shortcuts import render
from django.db.models import F
from django.db import transaction

# Create your views here.
from decimal import Decimal, ROUND_HALF_UP


# import this
from playground.models.product import Product
from playground.models.category import Category




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
    Product.objects.filter(category__name="Electronics").update(price=F("price") * 1.1)
    Product.objects.filter(category__name="Electronics").values("name", "price")
    with transaction.atomic():
        product = Product.objects.select_for_update().get(id=1)
        
        product.stock = product.stock - 1
        product.save()

    # Prevent
    #  💥 N+1 Disaster

    products = Product.objects.select_related("category").all()

    for product in products:
        print(product.name, product.category.name)
    """


    # ❌ View ساده ولی اشتباه (N+1)
    """
    مشکل؟

    اگر 100 Category داشته باشی → 101 Query

    N+1 سنگین

    افتضاح در scale
    """
    for category in Category.objects.all():
        product = (
            Product.objects
            .filter(category=category)
            .order_by("-price")
            .first()
        )
        print(category.name, product.name)

    return render(request, 'sina.html')