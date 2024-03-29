from apktau.settings_base import *
import dj_database_url
from dotenv import load_dotenv
load_dotenv()


DEBUG = True

SECRET_KEY = environ['SECRET_KEY']

ROOT_URLCONF = 'apktau.urls_dev'


DATABASES = {
    'default': dj_database_url.parse(environ['DATABASE_URL'])
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