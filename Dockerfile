FROM python:3.11-slim-bullseye

RUN apt-get update && \
    apt-get install -y ffmpeg && \
    apt-get clean autoclean && \
    apt-get autoremove --purge -y && \
    rm -rf /var/lib/apt/lists/* && \
    rm -f /var/cache/apt/archives/*.deb && \
    find /var/lib/apt -type f | xargs rm -f && \
    find /var/cache -type f -exec rm -rf {} \; && \
    find /var/log -type f | while read f; do echo -ne '' > $f; done;

RUN mkdir -p /usr/app

WORKDIR /usr/app

RUN pip install gunicorn poetry

COPY poetry.lock pyproject.toml /usr/app/

RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

COPY . /usr/app

EXPOSE 8000

ENV DJANGO_SETTINGS_MODULE=config.settings
ENV GUNICORN_BIND=0.0.0.0:8000
ENV GUNICORN_WORKERS=2
ENV GUNICORN_WORKERS_CONNECTIONS=1001
ENV GUNICORN_TIMEOUT=300
ENV GUNICORN_THREADS=2

CMD ["bash", "docker-startup.sh"]
