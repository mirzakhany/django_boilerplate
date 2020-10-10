from .base import *

DEBUG = (ENV_SETTING('DEBUG', 'true') == 'true')
TEMPLATE_DEBUG = (ENV_SETTING('TEMPLATE_DEBUG', 'true') == 'true')
