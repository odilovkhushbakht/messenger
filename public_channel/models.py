from datetime import datetime

from django.db import models


# Create your models here.
from knox.models import User


class PublicChanel(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, verbose_name='Пользователи')
    admin = models.CharField(max_length=20, verbose_name='Имя пользователья')
    post_text = models.TextField(null=True, blank=True)
    post_img = models.ImageField(verbose_name='Медиафайлы', upload_to='media', null=True, blank=True)
    date = models.DateTimeField(default=datetime.now())
