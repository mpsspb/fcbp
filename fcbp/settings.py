# -*- coding: utf-8 -*-
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
secret_file = os.path.join(BASE_DIR, 'secret.txt')
SECRET_KEY = open(secret_file).read().strip()

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

# change default auth.user model on fcbp project
AUTH_USER_MODEL = 'users.User'

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'fcbp',
    'users',
    'products',
    'clients',
    'employees',
    'finance',
    'reports',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'fcbp.urls'

WSGI_APPLICATION = 'fcbp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


TEMPLATE_DIRS = (
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(BASE_DIR, "templates"),
)

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LOCALE_PATHS = (
    os.path.join(BASE_DIR, "locale"),
)

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = False

REST_FRAMEWORK = {
    'DATE_INPUT_FORMATS': (
        '%d.%m.%Y',    # '25.10.2006
    ),
    'DATETIME_INPUT_FORMATS': (
        '%d.%m.%Y %H:%M:%S',  # '25.10.2006 22:15:30'
        '%d.%m.%Y %H:%M',  # '25.10.2006 22:15'
    ),
    'COERCE_DECIMAL_TO_STRING': False,
    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    # 'PAGE_SIZE': 10,
}

DATE_INPUT_FORMATS = (
    '%d.%m.%Y',    # '25.10.2006
)

DATETIME_INPUT_FORMATS = (
    '%d.%m.%Y %H:%M:%S',  # '25.10.2006 22:15:30'
    '%d.%m.%Y %H:%M',  # '25.10.2006 22:15'
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

AVATAR_ROOT = os.path.join(BASE_DIR, "avatar")
AVATAR_URL = 'avatar/'

BROKER_URL = 'redis://127.0.0.1:6379/3'
CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/3'
BROKER_TRANSPORT_OPTIONS = {
    'priority_steps': range(10),
}
CELERY_QUEUES = {
    'default': {
        "exchange": "fcbp",
        "binding_key": "fcbp",
    }}
CELERYBEAT_SCHEDULE_FILENAME = os.path.join(BASE_DIR, "schedule-bmdp")
# CELERY_IMPORTS = ("answermachine.actions.tasks",)
CELERY_DEFAULT_QUEUE = 'default'
# CELERY_IGNORE_RESULT = True
CELERY_ACCEPT_CONTENT = ['pickle']
REDIS_CONNECT_RETRY = True

try:
    from .local_settings import *
except Exception as e:
    print("Unable import local settings : %s" % (e))
    exit(1)

try:
    from .sys_settings import *
except Exception as e:
    print("Unable import local settings : %s" % (e))
    exit(1)
