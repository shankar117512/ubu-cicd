from .base import *
 
DEBUG = False
ENVIRONMENT = 'staging'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
ALLOWED_HOSTS = ['creative-flow-staging.up.railway.app']
CSRF_TRUSTED_ORIGINS = ['https://creative-flow-staging.up.railway.app']
