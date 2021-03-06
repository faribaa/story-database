"""
Django settings for sos project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

import os
import django

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = os.environ.get('SECRET_KEY')

ADMINS = (('Josh', 'josh@spacedog.xyz'),)
EMAIL_SUBJECT_PREFIX = '[StoriesOfSolidarity] '

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['localhost:9000',
                 '*.herokuapp.com',
                 '*.storiesofsolidarity.org']

# Application definition

INSTALLED_APPS = (
    'raven.contrib.django.raven_compat',
    'wpadmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'storages',
    'allauth',
    'allauth.account',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_auth',
    'rest_auth.registration',
    'actstream',

    'people',
    'stories'
)

MIDDLEWARE_CLASSES = (
    'django.middleware.cache.UpdateCacheMiddleware',

    'sslify.middleware.SSLifyMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'sms.middleware.RequestCookies',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'django.middleware.cache.FetchFromCacheMiddleware',
)

from django.conf import global_settings
TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
    "django.core.context_processors.request",
)

ROOT_URLCONF = 'sos.urls'

WSGI_APPLICATION = 'sos.wsgi.application'


# Cross Origin Resource Sharing
CORS_ORIGIN_REGEX_WHITELIST = (
    # allow CORS requests from our servers
    '^https?:\/\/(\w+\.)?herokuapp\.com$',
    '^https?:\/\/(\w+\.)?storiesofsolidarity\.org$',
    '^https?:\/\/(\w+\.)?spacedog\.xyz$',
    # and transifex
    '^https?:\/\/[\w\-\.]+transifex.com$',  # with nested subdomains
)
CORS_ALLOW_CREDENTIALS = True
CORS_URLS_REGEX = r'^/api/.*$'

CORS_ALLOW_HEADERS = (
    'x-requested-with',
    'content-type',
    'accept',
    'origin',
    'authorization',
    'x-csrftoken',

    # not sure why these are required, but they are showing up
    # when DefaultRouter.trailing_slash = True to allow consistent URLs
    'dnt',
    'cache-control',
    'accept-encoding'
)

# REST Framework
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': ('rest_framework.authentication.TokenAuthentication', ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 50,
    'DEFAULT_PERMISSION_CLASSES': (
        'sos.permissions.IsAuthorOrReadOnly',
    )
}
APPEND_SLASH = True

# REST Authentication
REST_SESSION_LOGIN = False

# for email-only logins
# ACCOUNT_AUTHENTICATION_METHOD = 'email'
# ACCOUNT_EMAIL_REQUIRED = True
# ACCOUNT_USERNAME_REQUIRED = False

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",  # for admin
    "allauth.account.auth_backends.AuthenticationBackend",  # for rest
)

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Caches
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}
# SESSION_ENGINE = "django.contrib.sessions.backends.cache"

TEMPLATE_DIRS = (os.path.join(BASE_DIR, "sos", "templates"), os.path.dirname(django.__file__))

SITE_ID = 1

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Email
EMAIL_HOST = 'localhost'
SERVER_EMAIL = 'info@storiesofsolidarity.org'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

MEDIA_ROOT = 'media'

# Twilio
TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN')

# Mapzen
MAPZEN_KEY = 'search-0w-fs0s'

# us-data local hosting
ZIPCODE_LOOKUP_URL = 'http://localhost:3000/geography/zipcodes/all/%s.geo.json'

# Amazon S3
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
AWS_STORAGE_BUCKET_NAME = "storiesofsolidarity"
AWS_QUERYSTRING_AUTH = False
