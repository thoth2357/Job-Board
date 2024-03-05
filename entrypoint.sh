#!/bin/bash
echo "Starting jobwebsite application..."

# Apply database migrations
echo "Apply database migrations"
poetry run python manage.py migrate

# Start server
echo "Starting server"
poetry run python manage.py runserver 0.0.0.0:7000

# Start celery
echo "Starting celery"
celery -A jobWebsite worker -E -l info --logfile=celery.log

# Start celery beat
echo "Starting celery beat"
celery -A jobWebsite beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler