from django.contrib.auth.models import AbstractUser, Group
from django.db import models

class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True,verbose_name='имя пользователя',help_text='Введите имя пользователя')
    email = models.EmailField(max_length=50,unique=True, verbose_name='Email', help_text='Введите email')
    email_verified = models.BooleanField(default=False, verbose_name='Email подтвержден')

    ROLE_CHOICES = [
        ('user', 'Пользователь'),
        ('manager', 'Менеджер'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'