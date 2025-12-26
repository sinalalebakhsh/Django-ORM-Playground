## Steps:

1.

```
pipenv install django
```

2.

```
pipenv shell
```

3. in vscode:
   Ctrl + P
4. write:

```
Python Select interpreter
```

5. Check:

```
django-admin --version
```

Result have 6.0 or higher:

> 6.0

6.

```
django-admin startproject orm_playground
```

7.

```
cd orm_playground
```

Current structure:

```
orm_playground/
├── orm_playground/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
└── manage.py
```

8. in this directory: /Django-ORM-Playground/orm_playground

```
python manage.py startapp playground
```

Current structure:

```
orm_playground/
├──orm_playground/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├──manage.py
│
├──playground/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
```

In orm_playground/settings.py:

```
INSTALLED_APPS = [
    ...
    'playground',
]
```

9. First project implementation (health check) directory -> /Django-ORM-Playground/orm_playground

```
python manage.py runserver
```

Result in Terminal VScode:

> Watching for file changes with StatReloader
> Performing system checks...
>
> System check identified no issues (0 silenced).
>
> You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
> Run 'python manage.py migrate' to apply them.
> December 21, 2025 - 12:13:11
> Django version 6.0, using settings 'orm_playground.settings'
> Starting development server at [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
> Quit the server with CTRL-BREAK.
>
> WARNING: This is a development server. Do not use it in a production setting. Use a production WSGI or ASGI server instead. Use a production WSGI or ASGI server instead.
> For more information on production servers see: [https://docs.djangoproject.com/en/6.0/howto/deployment/](https://docs.djangoproject.com/en/6.0/howto/deployment/)

---



## چرا این شروع «درسته»؟

چون:

* **محیطت ایزوله‌ست (pipenv)**
  تمام وابستگی‌ها داخل یک virtual environment مشخص نصب می‌شن و پروژه به سیستم عامل وابسته نمی‌مونه.

* **نسخه Django مشخصه**
  نسخه فریم‌ورک معلوم و قابل بررسیه؛ هر کسی پروژه رو اجرا کنه، همون رفتار رو می‌بینه.

* **پروژه قابل انتشار و بازتولیده**
  این ساختار برای GitHub، تیم، مصاحبه شغلی و حتی محیط Production قابل اتکاست.

* **مسیر اجرا شفافه**
  بعداً هر کسی README یا این فایل رو بخونه، بدون حدس زدن دقیقاً همین مسیر رو می‌ره و به نتیجه می‌رسه.


10.Install in Terminal 
```
  pipenv install mysqlclient
```

11. Install MySQL 9.5 Command Line Client
[Click here...](https://dev.mysql.com/downloads/shell/)
OR
[Click here...](https://dev.mysql.com/doc/mysql-shell/9.5/en/)

12. Open MySQL 9.5 Command Line Client
```
  CREATE DATABASE orm_playground
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;
```
Result:
>Query OK, 1 row affected (0.160 sec)
>
>mysql>

13. Install mysql workbench
[Click here...](https://dev.mysql.com/downloads/workbench/)

14. in /Django-ORM-Playground/orm_playground
```
  python manage.py migrate
```
### result:
```
$ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying sessions.0001_initial... OK
```

#### الان اتفاق مهمی می‌افته:
Django ORM → MySQL

#### جدول‌های:
>auth_user
>
>django_migrations
>
>sessions
>
>admin

دقیقاً با SQL واقعی MySQL ساخته می‌شن

#### 📌 از این لحظه:
هر کوئری که بنویسی = SQL واقعی MySQL

#### چرا این مرحله برای ORM Playground حیاتی بود؟
* **چون از الان به بعد می‌تونیم:**
* **select_for_update() → lock واقعی**
* **transaction.atomic() → ACID واقعی**
* **race condition → واقعی**
* **performance → واقعی**
* **نه شبیه‌سازی SQLite ❌**

#### Django Admin دقیقاً چرا الان؟
* قبل از اینکه:
* example بنویسیم
* query پیچیده بزنیم
* transaction تست کنیم

#### ما نیاز داریم:
* دیتا سریع بسازیم
* نتیجه ORM رو ببینیم
* بدون نوشتن View و API تست کنیم
* 📌 Django Admin = کنسول تست ORM

15.
```
  python manage.py createsuperuser
```
نتیجه:
>Username (leave blank to use 'sina'): 
>Email address: 
>Password: 
>Password (again): 
>This password is too short. It must contain at least 8 characters.
>This password is too common.
>This password is entirely numeric.
>Bypass password validation and create user anyway? [y/N]: y
>Superuser created successfully.

16. 
```
  python manage.py makemigrations
```
result:
>Migrations for 'playground':
>  playground\migrations\0001_initial.py
>    + Create model Category
>    + Create model Product
17. 
```
  python manage.py migrate
```
>Operations to perform:
>  Apply all migrations: admin, auth, contenttypes, playground, sessions
>Running migrations:
>  Applying playground.0001_initial... OK

18. بررسی
```
$ python manage.py check
```
نتیجه:
>بررسی سیستم هیچ مشکلی را شناسایی نکرد (۰ بی‌صدا شد).

19. up server
```
  python manage.py runserver
```
>Watching for file changes with StatReloader
>Performing system checks...
>
>System check identified no issues (0 silenced).
>December 21, 2025 - 18:04:19
>Django version 6.0, using settings 'orm_playground.settings'
>Starting development server at http://127.0.0.1:8000/
>Quit the server with CTRL-BREAK.
>
>WARNING: This is a development server. Do not use it in a production setting. Use a production WSGI or ASGI server instead.
>For more information on production servers see: https://docs.djangoproject.com/en/6.0/howto/deployment/

20. داخل پنل ادمین چندتا دیتای فیک بساز

در Admin → Categories → Add

* این‌ها رو بساز (دقیقاً همین‌ها):

* Electronics

* Books

📌 عمداً کم و مشخص.

#### برای هر دسته حداقل ۳ محصول ایجاد کنید.

#### Electronics

* **Name:** iPhone
  **Price:** 1000
  **Stock:** 10
  **Active:** ✔️

* **Name:** Laptop
  **Price:** 2000
  **Stock:** 5
  **Active:** ✔️

* **Name:** Headphones
  **Price:** 200
  **Stock:** 30
  **Active:** ✔️

#### Books

* **Name:** Django Book
  **Price:** 50
  **Stock:** 100

* **Name:** Python Deep Dive
  **Price:** 70
  **Stock:** 60

#### چرا این دیتا؟
* قیمت‌ها متفاوت هستند
* مقدار stock متفاوت است
* بیش از یک category وجود دارد
* برای تست Bulk Update و سناریوهای ORM ایده‌آل است


## تست خیلی سریع ORM (Shell)
21. در دایرکتوری /Django-ORM-Playground/orm_playground
```
  python manage.py shell
  from playground.models.product import Product
  Product.objects.count()
```
result:
>5

22. in Django shell
```
  exit()
```
result:
>now exiting InteractiveConsole...


# Scenario 001 – Bulk UPDATE با Django ORM (MySQL)
# سناریو 001: افزایش قیمت محصولات یک دسته
### هدف سناریو

افزایش قیمت تمام Productهای یک Category مشخص به صورت **Bulk** و بررسی تفاوت روش‌های مختلف UPDATE در Django ORM.

در این سناریو یاد می‌گیریم:

* چرا `save()` برای bulk update خطرناک است
* چگونه `queryset.update()` کار می‌کند
* چرا استفاده از `F()` در MySQL حیاتی است
* مفهوم atomic update و جلوگیری از race condition

---

### سناریو مسئله

فرض کن می‌خواهیم:

> قیمت تمام Productهای دسته **Electronics** را ۱۰٪ افزایش دهیم.

---

### روش اشتباه (برای درک مشکل)

```python
# ❌ روش نادرست – save() داخل حلقه

products = Product.objects.filter(category__name="Electronics")

for product in products:
    product.price = product.price * 1.1
    product.save()
```

#### مشکلات این روش:

* به ازای هر Product یک Query اجرا می‌شود (N Query)
* در MySQL مستعد **race condition** است
* atomic نیست
* performance ضعیف

---

### روش درست (Bulk UPDATE با F)

```python
from django.db.models import F

Product.objects.filter(
    category__name="Electronics"
).update(
    price=F('price') * 1.1
)
```

#### مزایای این روش:

* فقط **یک Query** به MySQL ارسال می‌شود
* کاملاً atomic است
* مقدار قبلی price در خود دیتابیس استفاده می‌شود
* امن در برابر race condition
* بهترین انتخاب برای bulk update

---

### نتیجه مورد انتظار

* قیمت تمام Productهای Electronics افزایش پیدا می‌کند
* هیچ Productی از قلم نمی‌افتد
* عملیات سریع و ایمن انجام می‌شود

---

### نکته مهم ORM

> هر وقت مقدار جدید یک فیلد به مقدار قبلی همان فیلد وابسته است، **حتماً از `F()` استفاده کن**.

این قانون طلایی Django ORM است.


#### ❌ روش غریزی ولی اشتباه (خیلی‌ها همینو می‌زنن)
بریم داخل Django shell:
```
python manage.py shell
from playground.models.product import Product
products = Product.objects.filter(category__name="Electronics")
```
```
for product in products:
```
سپس
```
    product.price = product.price * 1.1
    product.save()
```
#####  
```
  >>> for product in products:
  ...     product.price = product.price * 1.1
  ...     product.save()
  ... 
  Traceback (most recent call last):
    File "<console>", line 2, in <module>
  TypeError: unsupported operand type(s) for *: 'decimal.Decimal' and 'float'
```
## 🧠 نتیجه ذهنی
| روش        | مشکل Decimal       | امن | سریع |
| ---------- | ------------------ | --- | ---- |
| for + save | ❌ باید دستی حل کنی | ❌   | ❌    |
| update + F | ✅ خودکار           | ✅   | ✅    |

23.Django shell
```
    python manage.py shell
```
```
  from playground.models.product import Product 
  Product.objects.filter(category__name="Electronics").values("name", "price")
``` 
Result:
>
><QuerySet [{'name': 'iPhone', 'price': Decimal('1771.56')}, {'name': 'Laptop', 'price': Decimal('3543.12')}, {'name': 'Headphones', 'price': Decimal('354.31')}]>
>

#### This:
```
  from django.db.models import F
  from playground.models import Product
  Product.objects.filter(
      category__name="Electronics"
  ).update(
      price=F("price") * 1.1
  )

```
####این خط:
* **بلافاصله اجرا می‌شود**
* **هیچ حلقه‌ای ندارد**
* **هیچ تابع save() ندارد**
* **هیچ خطای اعشاری/اعشاری ندارد**

#### 🧠 دقیقاً چه اتفاقی افتاد؟

برخلاف روش قبلی:
#### ❌ حلقه for**
* جنگو → داده‌ها را به پایتون وارد می‌کند
* پایتون → محاسبه می‌کند
* به پایگاه داده ارسال می‌کند
* پر از ریسک
#### ✅ F()
* جنگو فقط دستور را می‌دهد
* MySQL خودش قیمت را می‌خواند
* MySQL خودش قیمت را می‌نویسد
* همه چیز داخل پایگاه داده اتفاق می‌افتد

## 🧪 آزمون مهم (درک عمیق تفاوت)
حالا این را تصور کنید:
* ۱۰۰۰۰ محصول
* برای متد → ۱۰۰۰۱ پرس‌وجو
* متد F → ۱ پرس‌وجو
* اینجاست که ORM معنا پیدا می‌کند 🔥
## 🧠 قانون سرانگشتی که از این سناریو یاد گرفتید
* هر زمان که UPDATE به مقدار قبلی بستگی داشته باشد → F()
* بدون استثنا.

# 👉 Scenario 002 Transaction + select_for_update()

#### 🧠 قبل از کد: مشکل واقعی چیه؟

* فرض کن این Product رو داریم:

			
| id        | name     | price | stock |
| --------- | -------- | ---   | ----  |
| 1         |   iPhone | 1000  | 5     |

* حالا دو درخواست هم‌زمان میاد:
>
> Request A
>
* می‌خواد stock رو 1 تا کم کنه
>
> Request B
> 
* هم‌زمان می‌خواد stock رو 1 تا کم کنه

## ❌ اگر lock نداشته باشیم چی می‌شه؟

##### هر دو request اینو می‌خونن:
```
stock = 5
```

#### هر دو می‌نویسن:

```
stock = 4
```

#### ❗ نتیجه؟

دو تا فروش انجام شده
<br>
ولی stock فقط 1 تا کم شده
<br>
=> داده خراب (race condition واقعی)

24. 
## قدم ۱: ایمپورت‌ها
```
  from django.db import transaction
  from playground.models import Product
```

25. همزمان این کارها رو انجام میده یعنی 
<br>
 خط اول گرفتن محصول و آپدیت که خط سوم هست و خط چهارم که ذخیره هست ، همزمان باهم انجام میشه ولی اگه یک مورد به خطا بخوره هیچکدوم رو انجام نمیده.
 

```
with transaction.atomic():
    product = Product.objects.select_for_update().get(id=1)
    
    product.stock = product.stock - 1
    product.save()

```

#### 🧠 این کد دقیقاً چه کاری انجام می‌داد؟
1️⃣ transaction.atomic()
<br>
معنی:
<br>
یا همه تغییرات اعمال می‌شوند
<br>
یا اگر خطایی رخ دهد → همه چیز به حالت قبل برمی‌گردد
<br>
2️⃣ select_for_update()
<br>
معنی:
<br>
MySQL این سطر را قفل می‌کند
<br>
تا زمانی که این تراکنش کامل شود:
<br>
هیچ درخواست دیگری نمی‌تواند این محصول را به‌روزرسانی کند
<br>
حتی نمی‌تواند select_for_update() را فراخوانی کند
<br>
3️⃣ قفل فقط روی آن سطر است
<br>
کل جدول قفل نشده است
<br>
فقط محصولی با شناسه ۱


#### ❌ روش اشتباه (خیلی رایج)
```
  product = Product.objects.get(id=1)
  product.stock -= 1
  product.save()

```

#### 🧠 تفاوت Scenario 001 و 002
| سناریو | ابزار                             | کاربرد      |
| ------ | --------------------------------- | ----------- |
| 001    | `F()`                             | bulk update |
| 002    | `transaction + select_for_update` | update حساس |


### ⚠️ نکات خیلی مهم MySQL
🔹 فقط روی InnoDB کار می‌کنه
<br>
(خوشبختانه MySQL پیش‌فرض همینه)
<br>
🔹 بیرون transaction بی‌معنیه
<Br>
❌ این اشتباهه:

```
Product.objects.select_for_update().get(id=1)
```
بدون atomic() → هیچ lockی اتفاق نمی‌افته
#### 🧠 قانون طلایی Scenario 002
<br>
هر وقت:
<br>
چند مرحله update داری
<br>
یا موجودی / پول / سهم
<br>
transaction + select_for_update واجبه


# 👉 Scenario 003

## N+1 Problem + select_related / prefetch_related
<br>
(جایی که ۹۰٪ پروژه‌ها کند می‌شن بدون اینکه بفهمن چرا)
<br>


# 🚨 Scenario 003 – N+1 Problem + select_related و prefetch_related


#### 🧪 سناریوی ساده (ولی فاجعه‌بار)
```
  from playground.models import Product

  products = Product.objects.all()

  for product in products:
      print(product.name, product.category.name)

```



# 💥 فاجعه N+1

فرض کن:
<br>
1,000 تا Product داری
<br>
کوئری‌هایی که اجرا می‌شن:
<br>
1️⃣ یک query:

```
SELECT * FROM product;
```

2️⃣ برای هر Product:

```
SELECT * FROM category WHERE id = ...
```

یعنی:
<br>
1 + 1000 = 1001 Query 😱
<br>
و تو حتی متوجهش نمی‌شی.
<Br>
🧠 چرا این اتفاق می‌افته؟
<br>
چون:
<br>
category یک ForeignKey است
<br>
Django به‌صورت lazy لود می‌کنه
<br>
هر بار که می‌گی:

```
product.category
```
→ یک query جدید می‌زنه


#### ✅ راه‌حل ۱: select_related (برای ForeignKey)

~~~
products = Product.objects.select_related("category").all()

for product in products:
    print(product.name, product.category.name)

~~~

🔥 این بار چه شد؟
<br>
Django این کار رو می‌کنه:
<br>

```
SELECT product.*, category.*
FROM product
JOIN category ON ...
```
#### 🧠 قانون select_related

* **فقط برای:**
* ForeignKey
* OneToOneField
* ❌ برای ManyToMany مناسب نیست

### ✅ راه‌حل ۲: prefetch_related (برای Many)
حالا فرض کن:
<br>
هر Product چندتا Tag داره
<br>

```
for product in products:
    for tag in product.tags.all():
        print(tag.name)
```
اینم N+1 وحشتناک 😬
<br>
راه درست:

```
products = Product.objects.prefetch_related("tags").all()
```

#### Django:
1 query برای Product
<br>
1 query برای Tag
<br>
بعد تو Python وصلشون می‌کنه

#### 🧠 تفاوت خیلی مهم
| ابزار            | JOIN         | تعداد Query |
| ---------------- | ------------ | ----------- |
| select_related   | SQL JOIN     | 1           |
| prefetch_related | Python-level | 2           |

# 🧠 قانون طلایی Scenario 003

>قبل از نمایش لیست‌ها:
>همیشه به N+1 فکر کن
>

🧪 تمرین پیشنهادی (خیلی مهم)
<br>
این رو بزن و تفاوت رو حس کن:
<br>
django shell:

```
from django.db import connection

len(connection.queries)

```


#### ❌ View ساده ولی اشتباه (N+1)
```
def product_list(request):
    products = Product.objects.filter(
        category__name="Electronics"
    ).order_by("price")

    for product in products:
        print(product.category.name)

    return HttpResponse("OK")
```
<br>

* **مشکل؟**
> 
> برای هر product → یک query به category
> 
> اگر 500 product داشته باشی → 501 query
> 

#### ✅ View درست و حرفه‌ای
```
def product_list(request):
    products = (
        Product.objects
        .select_related("category")
        .filter(category__name="Electronics")
        .order_by("price")
    )

    for product in products:
        print(product.name, product.category.name, product.price)

    return HttpResponse("OK")
```

🧠 چرا ترتیب مهمه؟
<br>
این‌ها از نظر ORM معنای ذهنی دارن:

```
Product.objects
.select_related("category")   # داده مرتبط رو از قبل بگیر
.filter(...)                  # بعد فیلتر کن
.order_by(...)                # بعد مرتب کن
```
🔍 SQL ذهنی که Django می‌سازه
<br>

```
SELECT product.*, category.*
FROM product
JOIN category ON product.category_id = category.id
WHERE category.name = 'Electronics'
ORDER BY product.price ASC;
```

# 🧪 تمرین خیلی مهم
in django shell

```
products = Product.objects.filter(category__name="Electronics").order_by("price")
```
```
for product in products:
    print(product.name, product.category.name)
```
## نتیجه:
>
>... 
>Headphones Electronics
>iPhone Electronics
>Laptop Electronics
>
```
from django.db import connection
len(connection.queries)
```
## نتیجه:
>
> 8
>
#### Step 5: خروج
```
exit()
```
<br>
## کوئری بهینه:

```
products = (Product.objects.select_related("category").filter(category__name="Electronics").order_by("price"))
```
سپس:
```
for product in products:
    print(product.name, product.category.name)
```
## نتیجه:
>
>... 
>Headphones Electronics
>iPhone Electronics
>Laptop Electronics
>
سپس
```
len(connection.queries)
```
>
> 3
>

🧠 اگر می‌خواهید «خود SQL» را ببینید
```
for q in connection.queries:
    print(q["sql"])
```

# 🔥 Scenario 005 – Subquery و OuterRef
اینجا جاییه که:
* **ORM از «Query ساده» تبدیل می‌شه به SQL ذهنی**
* **خیلی‌ها بلد نیستن**

#### 🎯 مسئله واقعی
سناریو:

* برای هر Category، می‌خوای:
* گران‌ترین Product اون Category رو بگیری
* و اسم و قیمتش رو نمایش بدی


26. in root project directory
```
pipenv install django-debug-toolbar
```
27. See this
[Click here...](https://django-debug-toolbar.readthedocs.io/en/latest/index.html)


#### مشکل؟

اگر 100 Category داشته باشی → 101 Query
<br>
N+1 سنگین
<br>
افتضاح در scale 

```
    for category in Category.objects.all():
        product = (
            Product.objects
            .filter(category=category)
            .order_by("-price")
            .first()
        )
        print(category.name, product.name)
```

# مسئله اصلی چیه؟

تو وقتی ORM ساده می‌نویسی، هر Query روی یک جدول اجرا می‌شه
<br>
ولی بعضی وقت‌ها می‌خوای بگی:
<br>

* **«برای هر ردیف از جدول A**
* **یه Query روی جدول B بزن**
* **که به همون ردیف فعلی مربوطه»**
* **اینجا ORM معمولی کم میاره → Subquery + OuterRef وارد می‌شن.**

یک پرس و جو فرعی یک پرس و جو است که در داخل پرس و جو دیگری قرار گرفته است. در Django ORM، پرس و جوهای فرعی به شما کمک می کنند تا داده ها را از مدل های مرتبط در یک تماس پایگاه داده واکشی یا فیلتر کنید. این به ویژه زمانی مفید است که باید با داده های مرتبط کار کنید اما می خواهید چیزها را تمیز و کارآمد نگه دارید.

#### اول ذهنیت SQL رو درست کنیم (خیلی مهم)

##### فرض کن اینو می‌خوای:

* برای هر Category
* تعداد Product‌های داخلش رو حساب کن

در SQL خام (مفهومی):
```
SELECT
  category.*,
  (
    SELECT COUNT(*)
    FROM product
    WHERE product.category_id = category.id
  ) AS product_count
FROM category;
```

❗ دقت کن:
<br>
category.id مال query بیرونیه
<Br>
ولی داره داخل SELECT COUNT(*) ... استفاده می‌شه
<Br>
👉 این یعنی:
<Br>
مقدار ردیف بیرونی داره داخل subquery مصرف می‌شه

## حالا ترجمه این مفهوم به Django ORM
* **🎯 مشکل ORM**

تو Django نمی‌تونی مستقیم بنویسی:
```
Product.objects.filter(category_id=Category.id)
```
چون:

* **Category.id هنوز وجود نداره**
* **ORM هنوز روی «یک ردیف خاص» نرفته**


اینجاست که OuterRef معنی پیدا می‌کنه
<br>
تعریف خیلی ساده:
<br>

> OuterRef('id') یعنی:
> «وقتی ORM رفت روی یک Category خاص
> مقدار id همون ردیف رو اینجا بذار»

```
from django.db.models import OuterRef, Subquery, Count

products_count_subquery = (
    Product.objects
    .filter(category_id=OuterRef('id'))  # 👈 این خط کل داستانه
    .values('category_id')
    .annotate(cnt=Count('id'))
    .values('cnt')
)

categories = Category.objects.annotate(
    product_count=Subquery(products_count_subquery)
)
```

* **.filter(category_id=OuterRef('id'))**
یعنی:

> «وقتی ORM داره روی یک Category خاص می‌چرخه
> مقدار Category.id همون ردیف رو
> بذار جای OuterRef('id')»

# جمله طلایی (این رو حفظ کن)

> OuterRef یعنی پل ارتباطی بین Query بیرونی و Subquery

#### یا حتی ساده‌تر:

> «OuterRef می‌گه:
> مقدار این فیلد رو
> از ردیفی که الان روش هستیم بگیر»

## فرقش با filter معمولی چیه؟
```
Product.objects.filter(category_id=Category.id)
```
چرا غلطه؟
<br>
❌ غلط:

* **Category.id هنوز معنی نداره**
* **ORM هنوز روی ردیف خاصی نیست**

✅ درست:
```
Product.objects.filter(category_id=OuterRef('id'))
```
چون:

* **ORM می‌گه: «وقتش که رسید، مقدار رو می‌ذارم»**

# یک تشبیه خیلی ساده
## filter معمولی:

> «الان مقدار رو بده»

## OuterRef:

> «بعداً، وقتی رفتی روی هر ردیف، مقدارش رو بده»

# مسئله‌ای که Exists حل می‌کنه

بعضی وقت‌ها برات مهم نیست چندتا رکورد وجود داره
<br>
فقط می‌خوای بدونی:
<br>
«آیا حداقل یک رکورد مرتبط وجود دارد یا نه؟»
<br>
مثلاً:

* **آیا این Category حداقل یک Product دارد؟**
* **آیا این User حداقل یک Order دارد؟**
* **آیا این Product حداقل یک Review دارد؟**

اینجا:

* **Count زیاده**
* **Exists دقیقاً همون چیزیه که می‌خوای**

#### SQL ذهنی (خیلی مهم)
```
SELECT *,
  EXISTS (
    SELECT 1
    FROM product
    WHERE product.category_id = category.id
  ) AS has_products
FROM category;
```


نکته کلیدی:
<br>
category.id مال query بیرونی
<br>
داخل subquery استفاده شده
<br>
فقط TRUE / FALSE برمی‌گرده
<br>
ترجمه دقیق به Django ORM

```
from django.db.models import Exists, OuterRef

categories = Category.objects.annotate(
    has_products=Exists(
        Product.objects.filter(category_id=OuterRef('id'))
    )
)
```

تفاوت مهم Exists با Subquery + Count
<br>

| حالت           | پیشنهاد  |
| -------------- | -------- |
| فقط بله / خیر  | Exists   |
| تعداد مهمه     | Count    |
| مقدار خاص مهمه | Subquery |

# سناریوی بازارکاری واقعی (Order / User)
سناریو واقعی
<br>
فرض کن فروشگاه داری و می‌خوای:
<br>
کاربرانی را لیست کنی که حداقل یک سفارش پرداخت‌شده دارند
<br>

models:
```
class User(models.Model):
    email = models.EmailField()

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_paid = models.BooleanField(default=False)
```

## ساختار پیشنهادی حرفه‌ای (همونی که بازار می‌پسنده)
```
orm_playground/
├── orm_playground/
│   └── settings.py
│
├── playground/
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── order.py
│   │   ├── product.py
│   │   └── category.py
│   │
│   ├── admin.py
│   ├── apps.py
│   └── views.py
│
└── manage.py
```

چرا این ساختار درسته؟
<br>
1️⃣ چرا فولدر models/؟
<br>
چون:
<br>
پروژه بزرگ می‌شه
<br>
یک models.py بزرگ = فاجعه
<br>
هر مدل مسئولیت مشخص داره
<br>
2️⃣ چرا user.py داخل playground؟
<br>
چون:
<br>
این User مربوط به سناریو ORM توئه
<br>
نه User سیستمی Django
<br>
نه auth
<br>
📌 نکته خیلی مهم:
<br>
اگر از User واقعی Django استفاده می‌کنی → اصلاً مدل User نمی‌سازی
<br>
ولی اینجا ما User آموزشی / دامنه‌ای داریم



پیاده‌سازی صحیح قدم‌به‌قدم
<br>
📁 playground/models/user.py
<br>

```
from django.db import models

class User(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email
```
📁 playground/models/order.py
```
from django.db import models
from .user import User

class Order(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='orders'
    )
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f"Order #{self.id} - Paid: {self.is_paid}"
```
📁 playground/models/init.py (خیلی مهم)
```
from .user import User
from .order import Order
from .product import Product
from .category import Category
```
📌 اگر اینو ننویسی:

* **Django مدل‌ها رو نمی‌شناسه**
* **migrate به مشکل می‌خوره**

ثبت در admin (درسته)
<br>
📁 playground/admin.py

```
from django.contrib import admin
from .models import User, Order

admin.site.register(User)
admin.site.register(Order)
```

بعدش چی؟
<br>
حتماً: in Terminal

```
python manage.py makemigrations
```
### Result:
```
Migrations for 'playground':
  playground\migrations\0002_user_order.py
    + Create model User
    + Create model Order
```


```
python manage.py migrate
```
### Result:
```
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, playground, sessions
Running migrations:
  Applying playground.0002_user_order... OK
```

اگر این فایل نباشد یا اشتباه باشد چه می‌شود؟
<br>
❌ این اتفاق‌ها می‌افتد:
<br>
makemigrations مدل‌ها را کامل نمی‌بیند
<br>
admin.py ارور import می‌دهد
<br>
Queryها fail می‌شوند
<br>
پروژه در آینده شکننده می‌شود
<br>


# 🔴 Import Cycle یعنی چی؟ (تعریف خیلی ساده)

Import Cycle (Circular Import) یعنی:

* **دو (یا چند) فایل**
* **به‌صورت زنجیره‌ای**
* **همدیگه رو import کنن**
* **طوری که پایتون گیر بیفته**

یعنی پایتون نمی‌دونه اول کدوم رو کامل لود کنه.
<br>

مثال خیلی ساده (غیر Django)
<br>
file_a.py

```
from file_b import B

class A:
    pass
```
file_b.py

```
from file_a import A

class B:
    pass
```

❌ نتیجه:

```
ImportError: cannot import name 'A'
```

چرا؟

* **پایتون شروع می‌کنه file_a**
* **می‌رسه به file_b**
* **file_b می‌گه: اول file_a**
* **پایتون: 😐**

# ❌ سناریوی خطرناک (خیلی رایج)
user.py

```
from .order import Order

class User(models.Model):
    pass
```

order.py

```
from .user import User

class Order(models.Model):
    user = models.ForeignKey(User, ...)
```
❌ این دقیقاً یک import cycle است
<br>
چون:

* **user → order**
* **order → user**

### Django چرا گاهی اینو تحمل می‌کنه و گاهی نه؟

چون:
<br>
Django موقع startup
<br>
مدل‌ها رو با App Registry
<br>
و ترتیب خاصی load می‌کنه
<br>
ولی:

* **در admin**
* **در shell**
* **در migrate**
* **در تست**

⚠️ ممکنه ناگهانی بترکه

## ✅ راه‌حل‌های حرفه‌ای (مم)
راه‌حل 1️⃣ (بهترین و استاندارد Django)
<br>
استفاده از string reference در ForeignKey
<br>
order.py (درست):

```
class Order(models.Model):
    user = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,
        related_name='orders'
    )
```
یا حتی امن‌تر:
```
class Order(models.Model):
    user = models.ForeignKey(
        'playground.User',
        on_delete=models.CASCADE
    )
```
#### 📌 این یعنی:

> «اسم مدل رو می‌گم،
> نه خود کلاس رو»

Django بعداً خودش resolve می‌کنه.

#### راه‌حل 2️⃣ (Import داخل تابع – فقط در موارد خاص)
```
def some_function():
    from .user import User
```
✔️ import تنبل (lazy)
<br>
❌ برای مدل‌ها توصیه نمی‌شه مگر مجبور باشی

# راه‌حل 3️⃣ (جدا کردن Domain)
وقتی دیدی:

* **user.py**
* **order.py**
* **payment.py**

همه دارن همدیگه رو import می‌کنن
<br>
🚨 یعنی معماری داره هشدار می‌ده

راه‌حل:

* **Domain رو split کن**
* **App جدا بساز**

#### نقش __init__.py در import cycle

__init__.py
```
from .user import User
from .order import Order
```
### ⚠️ اگر داخل user.py دوباره order رو import کنی:
* **import دوطرفه می‌شه**
* **احتمال cycle بالا می‌ره**

# 📌 قانون:

* **مدل‌ها فقط به string reference تکیه کنن**
* **نه import مستقیم**

# قانون طلایی (این رو حفظ کن)

* ***Model → Model = string reference***
* ***Service / Query → import واقعی***

