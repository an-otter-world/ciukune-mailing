"""Urls for ciukune core."""
from sys import stdout
from django.urls import include
from django.urls import path
from django.urls import re_path


def _get_api_url():
    return include([
    ])

urlpatterns = [
    re_path(r'api/', _get_api_url()),
]
