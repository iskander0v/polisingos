from polisingos.settings.common import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
     #('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',# 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'polisingos',                      # Or path to database file if using sqlite3.
        'USER': 'polisingos',                      # Not used with sqlite3.
        'PASSWORD': 'avt902119',                  # Not used with sqlite3.
        'HOST': 'localhost',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}
MEDIA_ROOT = ''
MEDIA_URL = ''
STATIC_ROOT = ''
STATIC_URL = '/static/'
STATICFILES_DIRS = ()
TEMPLATE_DIRS = ('C:/Users/riskanderov.PROJECTX/Documents/GitHub/polisingos/templates',)
