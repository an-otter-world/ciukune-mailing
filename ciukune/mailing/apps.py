"""Ciukune mailing urls."""
from os.path import dirname
from typing import Iterable

from django.urls import include
from django.urls import path
from django.urls import re_path
from django.urls.resolvers import URLPattern

from ciukune.core import CiukuneAppConfig

_OBJECT_VIEW_MAPPING = {
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
}

class AppConfig(CiukuneAppConfig):
    """AppConfig implementation for ciukune core."""
    name = 'ciukune.mailing'
    label = 'ciukune_mailing'
    path = dirname(__file__)

    def get_urls(self) -> Iterable[URLPattern]:
        from .views.test import TestView
        from ciukune.mailing.views.mail import MailViewSet
        from ciukune.core.serializers.user import UserSerializer
        UserSerializer.add_field_name('mail_set')

        yield re_path(r'api/',
            include([
                path('test', TestView.as_view(), name='test'),
                path('mails/<int:pk>', MailViewSet.as_view(_OBJECT_VIEW_MAPPING), name='mail-detail'),
            ])
        )
