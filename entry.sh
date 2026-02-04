#!/bin/sh
set -e

echo "Running migrations..."
python manage.py makemigrations --noinput
python manage.py migrate --noinput

echo "Starting Gunicorn..."
exec gunicorn filmapp.wsgi:application --bind 0.0.0.0:8000
