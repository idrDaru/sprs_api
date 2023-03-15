# SPRS API

**Build Setup**
---

1. django
```pip install django```

2. rest framework
```pip install djangorestframework```

3. pygments
```pip install pygments```

3. environ
```pip install django-environ```

4. psycopg2-binary
```pip install psycopg2-binary```

5. pyjwt
```pip install pyjwt```


**Environment Setup**
---

1. create .env file on root folder project
```
SECRET_KEY=

DB_NAME=
DB_USER=
DB_PASSWORD=
DB_HOST=
DB_PORT=
```

2. generate secret key 
```python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'```

3. Database migration
```
python manage.py makemigrations api
python manage.py migrate api
```


**Run Project**
---

1. Serve Project
```python manage.py runserver```
