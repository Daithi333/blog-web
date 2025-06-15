#!/bin/sh

set -eu

if [ "$ENV" = "production" ]; then
    echo "Starting in production with Gunicorn..."
    poetry run gunicorn blogweb.wsgi:application --bind 0.0.0.0:8000
else
    echo "Starting in development with Django's runserver..."
    poetry run python src/manage.py runserver 0.0.0.0:8000
fi
