from .base import *

BASE_DIR = "/app"
SECRET_KEY = "this-is-for-build-only"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': "postgres",
        'USER': "postgres",
        'PASSWORD': "postgres",
        'HOST': "postgres",
        'PORT': "5432",
        'OPTIONS': {
            'connect_timeout': 3,
        }
    }
}


STATIC_ROOT = os.path.join(BASE_DIR, "static")

MEDIA_ROOT = "/tmp"
DEBUG = True
