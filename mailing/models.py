from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Mailing(models.Model):
    PERIOD_CHOICES = (
        ('ONCE', 'Единоразовая'),
        ('DAILY', 'Раз в день'),
        ('WEEKLY', 'Раз в неделю'),
        ('MONTHLY', 'Раз в месяц'),
    )

    STATUS_CHOICES = (
        ('CREATED', 'Создана'),
        ('STARTED', 'Запущена'),
        ('FINISHED', 'Завершена'),
    )

    datetime_start = models.DateTimeField(auto_now_add=True, verbose_name='время начала рассылки')
    datetime_finish = models.DateTimeField(auto_now=True, verbose_name='время окончания рассылки')
    period = models.CharField(max_length=25, choices=PERIOD_CHOICES, default='DAILY', verbose_name='периодичность')
    status = models.CharField(max_length=25, choices=STATUS_CHOICES, default='CREATED', verbose_name='периодичность')

    customers = models.ManyToManyField('customers.Customer', verbose_name='Контакты клиентов')
    messages = models.ForeignKey('mail_messages.Message', on_delete=models.CASCADE, verbose_name='Сообщение')

    def __str__(self):
        return f'{self.datetime_start}-{self.datetime_finish}, {self.period}, {self.status}'

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'
