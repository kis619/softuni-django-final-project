#!/bin/sh
python manage.py wait_for_db
python manage.py makemigrations
python manage.py migrate --noinput
python manage.py collectstatic --noinput

exec gunicorn final_exam.wsgi:application --bind 0.0.0.0:8000
