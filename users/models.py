from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.tokens import default_token_generator
from secrets import token_hex
NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    phone = models.CharField(max_length=35, verbose_name='телефон', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    country = models.CharField(max_length=50, verbose_name='страна', **NULLABLE)
    verify_token = models.CharField(default=token_hex(6))
    is_active = models.BooleanField(default=False, verbose_name='активен')
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
