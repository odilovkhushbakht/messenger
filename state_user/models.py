from datetime import datetime

from django.db import models


# Create your models here.
from knox.models import User


class StateUser(models.Model):
    isActive = models.BooleanField(default=False, null=True, verbose_name='Пользователь в сети?')
    user = models.ForeignKey(User, null=True, blank=True, verbose_name='Пользователи')
    date = models.DateTimeField(default=datetime.now())