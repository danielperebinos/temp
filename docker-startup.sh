#!/bin/bash

echo "Collecting static files..."
python manage.py collectstatic --no-input

echo "Applying database migrations..."
python manage.py migrate --no-input

echo "Starting Gunicorn server..."
exec gunicorn --workers=${GUNICORN_WORKERS} config.wsgi:application -b ${GUNICORN_BIND} --log-level info --timeout ${GUNICORN_TIMEOUT} --max-requests-jitter ${MAX_REQUESTS_JITTER:-250} --max-requests ${GUNICORN_MAX_REQUESTS:-2500}