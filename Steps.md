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
    auth_user
    django_migrations
    sessions
    admin

دقیقاً با SQL واقعی MySQL ساخته می‌شن

#### 📌 از این لحظه:
    هر کوئری که بنویسی = SQL واقعی MySQL

#### چرا این مرحله برای ORM Playground حیاتی بود؟
چون از الان به بعد می‌تونیم:
select_for_update() → lock واقعی
transaction.atomic() → ACID واقعی
race condition → واقعی
performance → واقعی
نه شبیه‌سازی SQLite ❌

#### Why was this step crucial for ORM Playground?
Because from now on we can:
select_for_update() → real lock
transaction.atomic() → real ACID
race condition → real
performance → real
Not SQLite emulation ❌

