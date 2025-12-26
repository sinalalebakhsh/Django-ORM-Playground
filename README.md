# 🚀-Django-ORM-Playground
Build a Django project that:
* Focuses only on ORM Every scenario is executable + explainable + testable Can be easily extended later (blog, PDF, course)
[README FARSI](https://github.com/sinalalebakhsh/Django-ORM-Playground/blob/main/README_Farsi.md)


## Steps English:
[Click here...](https://github.com/sinalalebakhsh/Django-ORM-Playground/blob/main/Steps_English.md)

## 📌 Important note:
We don't teach ORM like a book → we treat it like a lab.

## 📌 This model is intentionally designed so that:
* F()
* bulk update
* race condition
* performance test
all methods are executable.


## How to run:

1. connect DATABASE (MySQL,Mongo,PostgreSQL,OR ...)
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'orm_playground',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': '1234',
        'OPTIONS': {
            'charset': 'utf8mb4',
        },
    }
}
```
2. Install dependencies (Pipfile):
```
pip install pipenv
```
than
```
pipenv install
```
3. use Environment:
```
pipenv shell
```
OR
<br>
Ctrl+P

> Python: Select Interpreter


5. MySQL Workbench:
Create a new SQL tab for executing queries:
<br>
Select first line and click on thunder ⚡
<br>
than select second line and click on thunder too:

```
DROP DATABASE orm_playground;
CREATE DATABASE orm_playground;
```
result:
> orm_playground created

* **if do not see it in Navigator -> SCHEMAS tab -> Right Click and Refresh all**
  
Now You can see it

4. run in Terminal/CMD
```
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
[Next Steps ... → ](https://github.com/sinalalebakhsh/Django-ORM-Playground/blob/main/Steps_English.md)
