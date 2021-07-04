"""Database settings, can be overrided in production."""
from os.path import join
from os.path import dirname
from os.path import abspath

BASE_DIR = dirname(dirname(abspath(__file__)))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': join(BASE_DIR, 'db.sqlite3'),
    }
}
