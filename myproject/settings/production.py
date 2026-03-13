from .base import *
 
DEBUG = False
ENVIRONMENT = 'production'

ALLOWED_HOSTS = ["*"]

STATIC_ROOT = BASE_DIR / "staticfiles"


SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
 
import sentry_sdk
sentry_sdk.init(
    dsn=config('SENTRY_DSN', default=''),
    environment='production',
    traces_sample_rate=0.1,
)
