from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models

from .enum import UserRoles


class User(AbstractUser):
    """Класс пользователя."""
    username = models.CharField(
        max_length=150,
        verbose_name='Логин',
        unique=True,
        validators=[RegexValidator(
            regex=r'^[\w.@+-]+$',
            message='Имя пользователя содержит недопустимый символ'
        )]
    )
    first_name = models.CharField(
        max_length=150,
        verbose_name='Имя пользователя',
        blank=True
    )
    last_name = models.CharField(
        max_length=150,
        verbose_name='Фамилия',
        blank=True
    )
    email = models.EmailField(
        max_length=254,
        verbose_name='email',
        unique=True
    )
    bio = models.TextField(
        verbose_name='Биография',
        blank=True
    )
    role = models.CharField(
        max_length=20,
        verbose_name='Роль',
        choices=UserRoles.choices(),
        default=UserRoles.user.name
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('id',)

    def __str__(self):
        return self.username

    @property
    def is_admin(self):
        return self.role == UserRoles.admin.name

    @property
    def is_moderator(self):
        return self.role == UserRoles.moderator.name

    @property
    def is_user(self):
        return self.role == UserRoles.user.name
