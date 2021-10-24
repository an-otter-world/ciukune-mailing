"""Mail views related class & utilities."""
from rest_framework.viewsets import ModelViewSet

from ciukune.mailing.models.mail import Mail
from ciukune.mailing.serializers.mail import MailSerializer

class MailViewSet(ModelViewSet):
    """Mail view set, providing standard user endpoints."""

    queryset = Mail.objects.all()
    serializer_class = MailSerializer
