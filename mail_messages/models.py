from django.db import models


class Message(models.Model):
    message_subject = models.CharField(max_length=100, verbose_name='Тема письма')
    text = models.TextField(verbose_name='Текст письма')

    def __str__(self):
        return self.message_subject

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'
