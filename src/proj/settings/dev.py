from .base import *  # noqa: F403

DEBUG = ENV_SETTING("DEBUG", "true") == "true"
TEMPLATE_DEBUG = ENV_SETTING("TEMPLATE_DEBUG", "true") == "true"

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}


# Disable caching while in development
CACHES = {
    "default": {
        "BACKEND": ENV_SETTING(
            "CACHE_BACKEND", "django.core.cache.backends.dummy.DummyCache"
        )
    }
}

# Add SQL statement logging in development
if ENV_SETTING("SQL_DEBUG", "false") == "true":
    LOGGING["loggers"]["django.db"] = {
        "handlers": ["console"],
        "level": "DEBUG",
        "propagate": False,
    }
