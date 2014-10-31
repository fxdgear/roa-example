from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


class DockerUserManager(BaseUserManager):

    def create_user(self, email, password=None):
        if not email:
            raise ValueError("We need an e-mail here...")

        user = self.model(
            email=DockerUserManager.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class DockerUser(AbstractBaseUser):
    username = models.CharField(max_length=254, unique=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'username'

    objects = DockerUserManager()

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin
