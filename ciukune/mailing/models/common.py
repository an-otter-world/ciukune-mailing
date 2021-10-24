"""Models common to all mailing application."""
from django.db.models import Model
from django.db.models import CharField
from django.db.models import ManyToManyField

from django.contrib.auth.models import Group


class Domain(Model):
    """A mailing domain."""

    name = CharField(null=False, blank=False)
    allowed_groups = ManyToManyField(Group)
    allowed_users = ManyToManyField(User)
