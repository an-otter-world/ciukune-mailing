from django.db.models import Model
from django.db.models import ForeignKey
from django.db.models import CASCADE
from django.db.models import CharField

from ciukune.core.models.user import User

class Mail(Model):
    name = CharField(max_length=100)
    user = ForeignKey(User, on_delete=CASCADE)
