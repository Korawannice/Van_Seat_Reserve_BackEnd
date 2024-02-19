from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    UserManager,
    Permission,
    Group,
)
from django.utils import timezone


ROLE = [("user", "User"), ("driver", "Driver"), ("admin", "Admin")]


class CustomUserManager(UserManager):
    def _create_user(self, username, email, password, **extra_fields):
        if not username:
            raise ValueError("A valid username is required")

        username = self.model.normalize_username(username)
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, username=None, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(
        self, username=None, email=None, password=None, **extra_fields
    ):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self._create_user(username, email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=11, unique=True, default="")
    email = models.EmailField(unique=True)
    prefix = models.CharField(max_length=100, blank=True, null=True)
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    tel = models.CharField(max_length=10, blank=True)
    role = models.CharField(max_length=20, choices=ROLE, default="user")
    last_login = models.DateTimeField(blank=True, null=True)

    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ["email"]
