from datetime import datetime

from django.db import models


# Create your models here.
from knox.models import User


class GroupChat(models.Model):
    group_name = models.CharField(max_length=150,  verbose_name='Название группы')
    text = models.TextField(verbose_name='Текст сообщение в группе', null=True, blank=True)
    on_user = models.CharField(max_length=200,  verbose_name='От пользователь')
    user = models.ForeignKey(User, null=True, blank=True, verbose_name='Пользователи')
    img = models.ImageField(verbose_name='Медиафайлы', upload_to='media', null=True, blank=True)
    date = models.DateTimeField(default=datetime.now())
