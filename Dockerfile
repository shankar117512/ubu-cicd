# Stage 1: Base ─────────────────────────────────────────────
FROM python:3.11-slim as base
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 PIP_NO_CACHE_DIR=1
WORKDIR /app
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential libpq-dev curl && rm -rf /var/lib/apt/lists/*
 
# Stage 2: Development ───────────────────────────────────────
FROM base as development
COPY requirements/development.txt .
RUN pip install -r development.txt
COPY . .
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
 
# Stage 3: Builder (install prod deps) ──────────────────────
FROM base as builder
COPY requirements/production.txt .
RUN pip install --prefix=/install -r production.txt
 
# Stage 4: Production ────────────────────────────────────────
FROM python:3.11-slim as production
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq5 && rm -rf /var/lib/apt/lists/*
 
# Create non-root user
RUN addgroup --system django && adduser --system --group django
 
WORKDIR /app
COPY --from=builder /install /usr/local
COPY --chown=django:django . .
RUN python manage.py collectstatic --noinput \
    --settings=myproject.settings.production
 
USER django
CMD ["gunicorn", "myproject.wsgi:application",
     "--bind", "0.0.0.0:$PORT", "--workers", "3", "--timeout", "120",
     "--access-logfile", "-"]
