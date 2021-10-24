"""Models relative to groups mailing management."""
from django.db.models import Model
from django.db.models import OneToOneField
from django.db.models import CASCADE
from django.db.models import CharField
from django.db.models import IntegerField
from django.db.models import ManyToManyField
from django.db.models import ForeignKey

from ciukune.core.models.user import User
from ciukune.mailing.models.common import Domain


class MailGroup(Model):
    """Mailing configuration for a group."""

    group: User = OneToOneField(User, on_delete=CASCADE, related_name='mailing')
    override_max_aliases = IntegerField(null=True)
    override_max_boxes = IntegerField(null=True)
    override_max_lists = IntegerField(null=True)


class List(Model):
    """Mailing list."""

    mail_group = ForeignKey(MailGroup, on_delete=CASCADE)
    address = CharField(null=False)
    domain = ForeignKey(Domain, on_delete=CASCADE)
    allowed_groups = ManyToManyField(Group)
    allowed_users = ManyToManyField(User)
