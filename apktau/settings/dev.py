from apktau.settings_base import *
import dj_database_url
from dotenv import load_dotenv
load_dotenv()


DEBUG = True

SECRET_KEY = environ['SECRET_KEY']

ROOT_URLCONF = 'apktau.urls_dev'


DATABASES = {
    'default': {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "apktau.sqlite3",

    }
}


INSTALLED_APPS += [
    'debug_toolbar',
    'django_browser_reload'
]


MIDDLEWARE += [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django_browser_reload.middleware.BrowserReloadMiddleware",


]


INTERNAL_IPS = [
    '127.0.0.1'
]


REST_FRAMEWORK["DEFAULT_RENDERER_CLASSES"] = [
    'rest_framework.renderers.JSONRenderer',
    'rest_framework.renderers.BrowsableAPIRenderer',
]
REST_FRAMEWORK["DEFAULT_PERMISSION_CLASSES"] = [
    # 'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    # 'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
]
