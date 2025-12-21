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
>6.0
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

```