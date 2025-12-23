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

## Why this start is correct

This setup is intentionally chosen to be **professional, reproducible, and publish-ready**.

* **Isolated environment (pipenv)**
  All dependencies are installed in an isolated virtual environment. This prevents system-wide conflicts and makes the project portable.

* **Explicit Django version**
  The Django version is fixed and verifiable. Anyone cloning the repository can reproduce the same behavior.

* **Publishable & reproducible project**
  The project can be cloned, installed, and run using the same steps on any machine.

* **Clear onboarding path**
  Anyone reading the README or this file can follow the exact same steps and reach the same working state without guessing.

---


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

#### Something important is happening now:
Django ORM → MySQL

#### Tables:
>auth_user
>
>django_migrations
>
>sessions
>
>admin

Built exactly with real MySQL SQL

#### 📌 From now on:
Any query you write = real MySQL SQL

#### Why was this step crucial for ORM Playground?
* **Because from now on we can:**
* **select_for_update() → real lock**
* **transaction.atomic() → real ACID**
* **race condition → real**
* **performance → real**
* **Not SQLite emulation ❌**

#### Django Admin Why exactly now?
* Before we:
* Write an example
* Run a complex query
* Test a transaction

#### We need to:
* Create data quickly
* See the ORM result
* Test without writing Views and APIs
* 📌 Django Admin = ORM testing console

15.
```
  python manage.py createsuperuser
```
result:
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

18. Check
```
  $ python manage.py check
```
result:
>System check identified no issues (0 silenced).

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

20. Create some fake data in the admin panel.

In Admin → Categories → Add

* Create these (exactly):

* Electronics

* Books

📌 Intentionally small and specific.

#### Create at least 3 products for each category.

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

#### Why this data?
* Prices are different
* Stock quantity is different
* There is more than one category
* Ideal for testing Bulk Update and ORM scenarios


## Very fast ORM (Shell) testing
21. in directory /Django-ORM-Playground/orm_playground
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


# Scenario 001 – Bulk UPDATE with Django ORM (MySQL)

### Scenario Goal

To increase the price of all products in a given Category in **Bulk** and examine the differences between different UPDATE methods in Django ORM.

In this scenario, we will learn:

* Why `save()` is dangerous for bulk update
* How `queryset.update()` works
* Why using `F()` in MySQL is crucial
* The concept of atomic update and avoiding race conditions

---

### Scenario Problem

Suppose we want to:

> Increase the price of all products in the **Electronics** category by 10%.

---

### Wrong method (to understand the problem)

```python
# ❌ Wrong method – save() inside a loop

products = Product.objects.filter(category__name="Electronics")

for product in products:
product.price = product.price * 1.1
product.save()
```

#### Problems with this method:

* One Query is executed for each Product (N Query)
* It is prone to **race condition** in MySQL
* Not atomic
* Poor performance

---

### Correct method (Bulk UPDATE with F)

```python
from django.db.models import F

Product.objects.filter(
category__name="Electronics"
).update(
price=F('price') * 1.1
)
```

#### Advantages of this method:

* Only **one Query** is sent to MySQL
* It is completely atomic
* The previous value of price is used in the database itself
* Safe against race condition
* The best choice For bulk update

---

### Expected result

* Price of all Electronics Products increases
* No Product is missed
* Operation is fast and secure

---

### ORM Important Point

> Whenever the new value of a field depends on the previous value of the same field, **Be sure to use `F()`**.

This is the golden rule of Django ORM.


#### ❌ Instinctive but wrong method (many do the same)
Let's go into the Django shell:
```
python manage.py shell
from playground.models.product import Product
products = Product.objects.filter(category__name="Electronics")
```
```
for product in products:
```
than
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
## 🧠 Mental result
| Method | Decimal Problem | Safe | Fast |
| ---------- | ------------------ | --- | ---- |
| for + save | ❌ You have to solve manually | ❌ | ❌ |
| update + F | ✅ Automatic | ✅ | ✅ |

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
####This line:
* **Runs immediately**
* **Has no loops**
* **Has no save()**
* **Has no Decimal / float errors**

#### 🧠 What exactly happened?

Unlike the previous method:
#### ❌ for-loop
* Django → pulls data into Python
* Python → calculates
* Sends back to database
* Full of risks
#### ✅ F()
* Django just gives the command
* MySQL reads the price itself
* MySQL writes the price itself
* Everything happens inside the database

## 🧪 Important test (deep understanding of the difference)
Now imagine this:
* 10,000 Products
* for method → ​​10,001 queries
* F method → ​​1 query
* This is where ORM makes sense 🔥
## 🧠 The rule of thumb you learned from this scenario
* Whenever UPDATE depends on the previous value → F()
* No exceptions.

# 👉 Scenario 002 Transaction + select_for_update()

#### 🧠 Before the code: What is the real problem?

* Suppose we have this Product:

| id | name | price | stock |
| -------- | -------- | --- | ---- |
| 1 | iPhone | 1000 | 5 |

* Now two requests come in at the same time:
>
> Request A
>
* wants to decrease stock by 1
>
> Request B
>
* wants to decrease stock by 1 at the same time

## ❌ What if we don't have a lock?

##### Both requests read:
```
stock = 5
```

#### Both write:

```
stock = 4
```

#### ❗ Result?

Two sales were made
<br>
But stock only decreased by 1
<br>
=> Corrupted data (real race condition)



