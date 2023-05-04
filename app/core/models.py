""""
    Database Models
"""

from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)


# User model manager
class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_field):
        """Create, Save and return a new user"""

        if not email:
            raise ValueError("Ueser must have an email address")

        # below code is same as defining a new object for model
        user = self.model(email=self.normalize_email(email), **extra_field)
        # encrypted password -> SHA256(one-way)
        user.set_password(password)
        # self._db if say we add multiple databases(good practice)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """Create and return superuser"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """User in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_Active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    # So user is able to login with the email
    USERNAME_FIELD = "email"
