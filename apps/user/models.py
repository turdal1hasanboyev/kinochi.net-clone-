from django.db import models

from django.contrib.auth.models import AbstractUser

from ckeditor.fields import RichTextField

from apps.common.models import BaseModel
from .manager import CustomUserManager


class User(BaseModel, AbstractUser):
    """User model."""

    """
    Fields:
    - username (str): none
    - email (str): unique=True
    first_name (str): null=True, blank=True
    last_name (str): null=True, blank=True
    """

    username = None
    email = models.EmailField(unique=True, db_index=True, max_length=50)
    first_name = models.CharField(max_length=150, blank=True, null=True, db_index=True)
    last_name = models.CharField(max_length=150, blank=True, null=True, db_index=True)

    image = models.ImageField(upload_to="users", blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True, db_index=True, unique=True)
    description = RichTextField(blank=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        """Meta class."""

        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        """Return string representation of user."""

        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        if self.phone_number:
            return f"{self.phone_number}"
        return f"{self.email}"
