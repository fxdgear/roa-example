from django.contrib.auth.models import AbstractBaseUser
from django.db import models

from django_roa import Model


class DockerUser(AbstractBaseUser, Model):
    id = models.IntegerField(unique=True)
    username = models.CharField(max_length=254, unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(blank=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', ]
