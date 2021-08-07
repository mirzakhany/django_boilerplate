"""
Django settings for proj project.

Generated by 'django-admin startproject' using Django 3.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
from pathlib import Path

import environ

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

# reading .env file
environ.Env.read_env()


def ENV_SETTING(key, default):
    return env.get_value(key, default=default)


if ENV_SETTING("ENABLE_SENTRY") == "True":

    integrations = [DjangoIntegration()]
    if ENV_SETTING("SENTRY_REDIS") == "True":
        from sentry_sdk.integrations.redis import RedisIntegration

        integrations.append(RedisIntegration())
    if ENV_SETTING("SENTRY_CELERY") == "True":
        from sentry_sdk.integrations.celery import CeleryIntegration

        integrations.append(CeleryIntegration())

    sentry_sdk.init(
        dsn=ENV_SETTING("SENTRY_DSN"),
        integrations=integrations,
        send_default_pii=True,
    )

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = Path(__file__).resolve().parents[2]

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "y#swzfnq4br$0vmcjs@yej^&qmv_tualw#(awwi=he@=!@#&8u"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ENV_SETTING("ALLOWED_HOSTS", "").split(",")
ALLOWED_HOSTS.append(ENV_SETTING("POD_IP", ""))

GIT_COMMIT = ENV_SETTING("GIT_COMMIT", "")


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "constance",
    "constance.backends.database",
    "corsheaders",
    "django_extensions",
    "rest_framework",
    "django_celery_beat",
    "apps.tasks_management",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "proj.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "proj.wsgi.application"

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "HOST": ENV_SETTING("POSTGRES_HOST", "localhost"),
        "NAME": ENV_SETTING("POSTGRES_NAME", "postgres"),
        "USER": ENV_SETTING("POSTGRES_USER", "postgres"),
        "PASSWORD": ENV_SETTING("POSTGRES_PASSWORD", "postgres"),
        "CONN_MAX_AGE": 0,
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation."
        "UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOCALE_PATHS = (str(BASE_DIR / "locale"),)
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = ENV_SETTING("STATIC_URL", "/static/")
STATIC_ROOT = os.path.join(BASE_DIR, "static")

# LOGGING
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
            "level": "INFO",
            "propagate": True,
        },
        "django.request": {
            "handlers": ["console"],
            "level": "ERROR",
            "propagate": False,
        },
        "proj": {
            "handlers": ["console"],
            "level": "DEBUG",
            "propagate": False,
        },
    },
}

# rest framework
REST_FRAMEWORK = {
    "DEFAULT_RENDERER_CLASSES": ("rest_framework.renderers.JSONRenderer",),
}

# redis configurations
REDIS_URL = "redis://{user}:{password}@{host}:6379/0".format(
    user=ENV_SETTING("REDIS_USER", ""),
    password=ENV_SETTING("REDIS_PASSWORD", ""),
    host=ENV_SETTING("REDIS_HOST", "0.0.0.0"),
)

# cache
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": REDIS_URL,
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "SOCKET_CONNECT_TIMEOUT": 5,  # in seconds
            "SOCKET_TIMEOUT": 5,  # in seconds,
            "IGNORE_EXCEPTIONS": True,
        },
    }
}

# celery
CELERY_TIMEZONE = TIME_ZONE
CELERY_BROKER_URL = REDIS_URL
CELERY_RESULT_BACKEND = REDIS_URL
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

TASKS_MANAGEMENT_QUEUE = 'tasks_management'

# django constance
CONSTANCE_BACKEND = "constance.backends.database.DatabaseBackend"
