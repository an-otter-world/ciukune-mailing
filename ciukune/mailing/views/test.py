"""Test plugged view."""
from rest_framework.views import APIView
from rest_framework.response import Response

class TestView(APIView):
    """User view set, providing standard user endpoints."""

    def get(self, request):
        return Response({'test': 'yipee'})
