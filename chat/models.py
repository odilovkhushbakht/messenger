
from datetime import datetime
from django.db import models


# Create your models here.
class Chat(models.Model):
    text = models.TextField(null=True, blank=True, verbose_name='Текст сообщение')
    on_user = models.CharField(max_length=200, verbose_name='От пользователь')
    to_user = models.CharField(max_length=200, verbose_name='К пользователью')
    img = models.ImageField(verbose_name='Медиафайлы', upload_to='media', null=True, blank=True)
    date = models.DateTimeField(default=datetime.now())









