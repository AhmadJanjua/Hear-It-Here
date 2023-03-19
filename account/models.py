# accounts/models.py
import datetime

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password, birthday, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        if not username:
            raise ValueError('The username field must be set')
        extra_fields.setdefault('date_joined', datetime.datetime.now())
        email = self.normalize_email(email)
        username = username.lower()

        user = self.model(email=email, username=username, birthday=birthday, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_moderator(self, email, username, password, birthday, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)
        return self.create_user(email, username, password, birthday, **extra_fields)

    def create_superuser(self, email, username, password, birthday=None, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, username, password, birthday, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, null=False, unique=True)
    username = models.CharField(max_length=50, null=False, unique=True)
    date_joined = models.DateTimeField(null=True)
    birthday = models.DateField(null=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'birthday']

    objects = CustomUserManager()

    def __str__(self):
        return self.username
