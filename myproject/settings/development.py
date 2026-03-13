from .base import *
 
DEBUG = True
ENVIRONMENT = 'development'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
CORS_ALLOW_ALL_ORIGINS = True
INSTALLED_APPS += ['debug_toolbar']
MIDDLEWARE = ['debug_toolbar.middleware.DebugToolbarMiddleware'] + MIDDLEWARE
CSRF_TRUSTED_ORIGINS = ["https://ubu-cicd-development.up.railway.app"]
ALLOWED_HOSTS = ['ubu-cicd-development.up.railway.app']
