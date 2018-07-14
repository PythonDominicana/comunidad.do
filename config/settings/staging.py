import logging

from .base import env
from .production import *


# GENERAL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = env('DJANGO_SECRET_KEY', default='fufOOEOpzM7mrd12EBzilmerFCkamtglCJtddghKiFHtJn201IIZrL0Zk5vpgPbb')
# https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS', default=['comunidad.do', 'comunidaddo.herokuapp.com'])

# DATABASES
# ------------------------------------------------------------------------------
DATABASES['default'] = env.db('DATABASE_URL')  # noqa F405
DATABASES['default']['ATOMIC_REQUESTS'] = True  # noqa F405
DATABASES['default']['CONN_MAX_AGE'] = env.int('CONN_MAX_AGE', default=60)  # noqa F405