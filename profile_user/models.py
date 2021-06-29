from django.db import models


# Create your models here.
class ProfilUser(models.Model):
    phone_number = models.IntegerField(max_length=12, null=True, blank=True, verbose_name='Номер телефон пользователья')
    name = models.CharField(max_length=20, verbose_name='Имя пользователья')