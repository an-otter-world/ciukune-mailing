from django.apps import AppConfig
from os.path import dirname

class Config(AppConfig):
    """AppConfig implementation for ciukune core."""
    name = 'ciukune.mailing'
    label = 'ciukune_mailing'
    path = dirname(__file__)
