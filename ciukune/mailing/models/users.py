"""Models relative to user mailing management."""
from django.db.models import Model
from django.db.models import OneToOneField
from django.db.models import CASCADE
from django.db.models import CharField
from django.db.models import IntegerField
from django.db.models import ForeignKey

from ciukune.core.models.user import User
from ciukune.mailing.models.common import Domain


class MailUser(Model):
    """Mailing configuration for a user."""

    user: User = OneToOneField(User, on_delete=CASCADE, related_name='mail')
    override_max_aliases = IntegerField(null=True)
    override_max_boxes = IntegerField(null=True)


class Alias(Model):
    """Mail alias to configured owner user's e-mail."""

    mail_user = ForeignKey(MailUser, on_delete=CASCADE)
    name = CharField(null=False, Blank=False)
    domain = ForeignKey(Domain, on_delete=CASCADE)


class Box(Model):
    """Mail box usable by a user."""

    mail_user = ForeignKey(MailUser, on_delete=CASCADE)
    name = CharField(null=False, Blank=False)
    domain = ForeignKey(Domain, on_delete=CASCADE)
