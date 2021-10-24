"""ciukune custom mail serializing & related utilities."""
from rest_framework.serializers import HyperlinkedModelSerializer

from ciukune.mailing.models.mail import Mail

class MailSerializer(HyperlinkedModelSerializer):
    """ciukune custom mail serializer.

    Keep the less possible stuff here. Use additionnal Django apps to add fields
    & features to the core mail, so they can be deactivated easily.
    """

    class Meta:
        model = Mail
        fields = ['name', 'user']
