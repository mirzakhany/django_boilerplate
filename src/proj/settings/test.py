# Settings file optimized for test running. Sets up in-memory database,
# Nose test runner and disables South for the tests

from .base import *

# Use in-memory SQLIte3 database for faster tests
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

# No need to use South in testing
SOUTH_TESTS_MIGRATE = False
SKIP_SOUTH_TESTS = True

# Disable cache
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

