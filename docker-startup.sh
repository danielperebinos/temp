#!/bin/bash

python manage.py collectstatic --no-input
python manage.py migrate --no-input
gunicorn --workers=${GUNICORN_WORKERS} config.wsgi:application -b ${GUNICORN_BIND} --log-level info --timeout ${GUNICORN_TIMEOUT}