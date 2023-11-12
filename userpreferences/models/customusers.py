from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from wheel.metadata import _


class CustomUser(AbstractUser):
    # İlişki çakışmalarını gidermek için related_name ekleyin
    groups = models.ManyToManyField(Group, verbose_name=_('groups'), blank=True, related_name='customuser_groups')
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_name='customuser_user_permissions',
    )