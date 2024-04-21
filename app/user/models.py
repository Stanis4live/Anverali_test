from django.db import models
from django.contrib.auth.models import AbstractUser

class Roles(models.TextChoices):
    CUSTOMER = 'CUSTOMER', 'Заказчик'
    PERFORMER = 'PERFORMER', 'Исполнитель'


class User(AbstractUser):
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    role = models.CharField('Роль', max_length=30, choices=Roles.choices)
    phone_number = models.CharField(max_length=20, unique=True)
    experience = models.IntegerField(default=0)

    def __str__(self):
        return self.username

