
# myapp/models.py
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin, BaseUserManager
)
from django.utils import timezone

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email manzili bo\'lishi shart')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser uchun is_staff=True bo\'lishi kerak')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser uchun is_superuser=True bo\'lishi kerak')

        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email         = models.EmailField('email address', unique=True)
    username      = models.CharField('username', max_length=150, unique=True)
    first_name    = models.CharField('first name', max_length=30, blank=True)
    last_name     = models.CharField('last name', max_length=30, blank=True)
    avatar        = models.ImageField(upload_to='avatars/', blank=True, null=True)
    bio           = models.TextField(blank=True)
    phone_number  = models.CharField(max_length=20, blank=True)

    is_staff      = models.BooleanField(default=False)
    is_active     = models.BooleanField(default=True)
    date_joined   = models.DateTimeField(default=timezone.now)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']  # email bilan birga kirishda talab qilinadigan maydonlar

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.email
