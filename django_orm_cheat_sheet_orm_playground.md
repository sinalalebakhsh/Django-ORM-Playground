# Django ORM Cheat Sheet

این Cheat Sheet از دل پروژه **Django-ORM-Playground** ساخته شده و بر اساس سناریوهایی است که واقعاً در پروژه استفاده می‌شوند.

---

## 1) QuerySet پایه

```python
from playground.models import Product

Product.objects.all()
Product.objects.first()
Product.objects.last()
Product.objects.count()
```

---

## 2) Filter / Exclude / Get

```python
Product.objects.filter(price__gt=100)
Product.objects.exclude(stock=0)
Product.objects.get(id=1)   # اگر نباشد: DoesNotExist
```

Lookupهای رایج:
- `__gt`, `__gte`, `__lt`, `__lte`
- `__icontains`, `__contains`
- `__in`, `__range`

---

## 3) ForeignKey Traversal

```python
Product.objects.filter(category__name="Electronics")
```

---

## 4) Order / Slice

```python
Product.objects.order_by("price")
Product.objects.order_by("-price")
Product.objects.all()[:10]
```

---

## 5) Bulk UPDATE (سناریو 001)

❌ روش اشتباه:
```python
for p in Product.objects.all():
    p.price += 10
    p.save()
```

✅ روش درست:
```python
from django.db.models import F

Product.objects.update(price=F("price") + 10)
```

قانون:
> هر وقت مقدار جدید به مقدار قبلی وابسته است → `F()`

---

## 6) Transaction + Lock (سناریو 002)

```python
from django.db import transaction

with transaction.atomic():
    product = Product.objects.select_for_update().get(id=1)
    product.stock -= 1
    product.save()
```

نکات:
- فقط روی MySQL InnoDB
- فقط داخل `atomic()` معنا دارد

---

## 7) N+1 Problem (سناریو 003)

❌ مشکل‌دار:
```python
products = Product.objects.all()
for p in products:
    print(p.category.name)
```

✅ بهینه:
```python
products = Product.objects.select_related("category")
```

قانون:
- `select_related` → ForeignKey / OneToOne
- `prefetch_related` → ManyToMany

---

## 8) Prefetch (ManyToMany)

```python
products = Product.objects.prefetch_related("tags")
```

---

## 9) Values / Values_list

```python
Product.objects.values("name", "price")
Product.objects.values_list("name", flat=True)
```

---

## 10) Exists

```python
Product.objects.filter(stock=0).exists()
```

سریع‌تر از `count() > 0`

---

## 11) Aggregate

```python
from django.db.models import Avg, Sum, Max

Product.objects.aggregate(Avg("price"))
Product.objects.aggregate(total=Sum("price"))
```

---

## 12) Annotate

```python
from django.db.models import Count

Category.objects.annotate(product_count=Count("product"))
```

---

## 13) Query Count & Profiling (سناریو 004)

```python
from django.db import connection

connection.queries.clear()
list(Product.objects.select_related("category"))
len(connection.queries)
```

دیدن SQL:
```python
for q in connection.queries:
    print(q["sql"])
```

---

## 14) Delete

```python
Product.objects.filter(stock=0).delete()
```

⚠️ برگشت‌پذیر نیست

---

## 15) Best Practices خلاصه

- Loop + save = خطر
- Bulk update = `update()`
- پول و عدد حساس = `DecimalField`
- لیست‌ها = حتماً N+1 را چک کن
- قبل از production → Query Count بگیر

---

این Cheat Sheet زنده است و با اضافه شدن سناریوهای جدید کامل‌تر می‌شود.

