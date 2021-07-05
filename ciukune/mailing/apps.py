"""Ciukune mailing urls."""
from os.path import dirname
from typing import Iterable

from django.urls import include
from django.urls import path
from django.urls import re_path
from django.urls.resolvers import URLPattern

from ciukune.core import CiukuneAppConfig

class AppConfig(CiukuneAppConfig):
    """AppConfig implementation for ciukune core."""
    name = 'ciukune.mailing'
    label = 'ciukune_mailing'
    path = dirname(__file__)

    def get_urls(self) -> Iterable[URLPattern]:
        from .views.test import TestView
        yield re_path(r'api/',
            include([
                path('test', TestView.as_view(), name='test'),
            ])
        )
