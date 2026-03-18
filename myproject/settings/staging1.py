from .base import *
 
DEBUG = False
ENVIRONMENT = 'staging1'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
ALLOWED_HOSTS = ['courageous-illumination-staging1.up.railway.app']
CSRF_TRUSTED_ORIGINS = ['https://courageous-illumination-staging1.up.railway.app']
