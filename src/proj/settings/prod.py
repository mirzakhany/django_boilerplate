from .base import *  # noqa: F40

DEBUG = ENV_SETTING("DEBUG", "true") == "true"
TEMPLATE_DEBUG = ENV_SETTING("TEMPLATE_DEBUG", "true") == "true"
