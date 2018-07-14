import logging

from .production import *

ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS', default=['staging-comunidaddo.herokuapp.com'])