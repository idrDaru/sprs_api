# SPRS API

## Build Setup

1. Install RabbitMQ
   `sudo apt install rabbitmq-server`
   or 
   https://www.rabbitmq.com/download.html

2. Python3.10

## **Install Dependencies**

1. install dependencies
   `pip install -r requirements.txt`

## **Environment Setup**

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
   `python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'`

3. Database migration

```
python manage.py makemigrations api
python manage.py migrate api
```

## **Run Project**

1. Serve Project
   `python manage.py runserver`

2. Run Flower Server
   `flower -A sprs_api --port=5555`

3. Run Celery Worker
   `celery -A sprs_api worker -l INFO`

4. Run Celery Bear
   `celery -A spsrs_api beat -l INFO`
