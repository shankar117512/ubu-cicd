import sys

from .base import *

DEBUG = True
ENVIRONMENT = "development"
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
CORS_ALLOW_ALL_ORIGINS = True
INSTALLED_APPS += ["debug_toolbar"]
MIDDLEWARE = ["debug_toolbar.middleware.DebugToolbarMiddleware"] + MIDDLEWARE
CSRF_TRUSTED_ORIGINS = ["https://ubu-cicd-development.up.railway.app"]
ALLOWED_HOSTS = [
    "healthcheck.railway.app",
    "ubu-cicd-development.up.railway.app",
    "localhost",
    "127.0.0.1",
]

if "pytest" in sys.modules:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": ":memory:",
        }
    }
