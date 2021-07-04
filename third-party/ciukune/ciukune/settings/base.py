"""Base settings settings."""
from os.path import dirname
from os.path import abspath
from os.path import join

BASE_DIR = dirname(dirname(abspath(__file__)))

DEBUG = True

APPEND_SLASH = False

ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'ciukune.oi.lan']

ROOT_URLCONF = 'urls'

LOGIN_URL = '/api-auth/login'

SECRET_KEY = 'secret_key'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'ciukune.Config',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    join(BASE_DIR, '.build', 'dist')
]

STATIC_ROOT = join(dirname(__file__), '..', '.static')
