from django.db import models

from users.models import User


class UsefulHabit(models.Model):
    """Модель полезной привычки."""
    title = models.CharField(max_length=35, verbose_name='название полезной привычки')
    place = models.CharField(max_length=35, verbose_name='название места')
    time = models.TimeField(verbose_name='время')
    action = models.CharField(max_length=50, verbose_name='название действия')
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name='Создатель полезной привычки',
                                related_name='user_useful_habit', null=True, blank=True)
    pleasant_habit = models.CharField(max_length=50, verbose_name='название приятной привычки')
    award = models.CharField(max_length=50, verbose_name='Вознаграждение за выполнение полезной привычки')
    sign_publicity = models.CharField(max_length=50, verbose_name='Публичная полезная привычка или нет?',
                                      choices=(('public', 'Публичная'), ('non-public', 'Непубличная')))
    class Meta:
        verbose_name = 'Полезная привычка'
        verbose_name_plural = 'Полезные привычки'

    def __str__(self):
        return f'{self.title}'
