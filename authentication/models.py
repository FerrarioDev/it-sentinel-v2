from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

AREA = (
    ('AFTERMARKET','Aftermarket'),
    ('IT','IT'),
    ('ADMINISTRATION','Administration'),
    ('PRODUCTION','Production'),
    )

class CustomUserManager(BaseUserManager):
    def create_user(self, dnarId, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(dnarId=dnarId, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, dnarId, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(dnarId, email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    dnarId = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    area = models.CharField(max_length=255, choices=AREA, default='IT')

    objects = CustomUserManager()

    USERNAME_FIELD = 'dnarId'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.dnarId
