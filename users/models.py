from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    """Модель пользователя."""
    username = None

    email = models.EmailField(verbose_name='Почта', unique=True)
    tg_nick = models.CharField(max_length=50, blank=True, null=True, verbose_name='Телеграмм ник')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email
