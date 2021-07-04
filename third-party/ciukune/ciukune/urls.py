"""Urls for ciukune core."""
from sys import stdout
from django.urls import include
from django.urls import path
from django.urls import re_path
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView

from ciukune.views.user.me import MeView
from ciukune.views.user import UserViewSet

_LIST_VIEW_MAPPING = {
    'get': 'list',
}

_OBJECT_VIEW_MAPPING = {
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
}

def _get_api_url():
    return include([
        path('auth/login', TokenObtainPairView.as_view(), name='login'),
        path('auth/refresh', TokenRefreshView.as_view(), name='refresh'),
        path('user/me', MeView.as_view(), name='me'),
        path('user', UserViewSet.as_view(_LIST_VIEW_MAPPING), name='user'),
        path('user/<int:pk>', UserViewSet.as_view(_OBJECT_VIEW_MAPPING), name='user_detail'),
    ])

urlpatterns = [
    re_path(r'api/', _get_api_url()),
    re_path(r'^(?!api).*$', TemplateView.as_view(template_name="index.html"), name="index"),
]
