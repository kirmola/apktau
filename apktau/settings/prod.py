from apktau.settings_base import *
from django.core.management.utils import get_random_secret_key
import dj_database_url
from os import environ


DEBUG = False

ROOT_URLCONF = 'apktau.urls'

ALLOWED_HOSTS = ["*"]

SECRET_KEY = str(get_random_secret_key())


DATABASES = {
    "default": dj_database_url.parse(environ["DATABASE_URL"])
}

REST_FRAMEWORK["DEFAULT_RENDERER_CLASSES"] = [
    'rest_framework.renderers.JSONRenderer',
]

REST_FRAMEWORK["DEFAULT_PERMISSION_CLASSES"] = [
    'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
]