from django.db import models


# Create your models here.
from knox.models import User


class ProfilUser(models.Model):
    phone_number = models.IntegerField(max_length=12, null=True, blank=True, verbose_name='Номер телефон пользователья')
    name = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Имя пользователья')