"""Tovarich core app."""
from os.path import dirname
import django.apps

class AppConfig(django.apps.AppConfig):
    """AppConfig implementation for ciukune core."""
    name = 'ciukune'
    label = 'ciukune_core'
    path = dirname(__file__)
