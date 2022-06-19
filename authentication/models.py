from core.models import TimeStampAbstractModel
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import BooleanField, EmailField
from django.utils.translation import gettext_lazy as _
# using versatile for image
from versatileimagefield.fields import VersatileImageField

from .managers import CustomUserManager


class User(AbstractUser, TimeStampAbstractModel):
    """Default user for tlms."""

    email = EmailField(_("Email Address"), unique=True, null=True, blank=True)
    email_verified = BooleanField(default=False)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=20)
    image = VersatileImageField(
        'Profile Picture',
        upload_to='profile/',
        null=True,
        blank=True
    )

    signature = VersatileImageField(
        'Signature',
        upload_to='documents/',
        null=True,
        blank=True
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

