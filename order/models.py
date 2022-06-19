from cmath import e
from pyexpat import model
from django.db import models
from core.models import TimeStampAbstractModel
from django.contrib.auth import get_user_model
from versatileimagefield.fields import VersatileImageField

User = get_user_model()

STATUS = (
    ('ACTIVE','active'),
    ('INACTIVE','inactive')
)

class Event(TimeStampAbstractModel):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    image = VersatileImageField(
        'Profile Picture',
        upload_to='profile/',
        null=True,
        blank=True
    )
    status = models.CharField(max_length=20,choices=STATUS)


    def __str__(self):
        return self.title



NEWS_STATUS = (
    ('EXPIRED','active'),
    ('INACTIVE','inactive')
)


class News(TimeStampAbstractModel):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    image = VersatileImageField(
        'Profile Picture',
        upload_to='profile/',
        null=True,
        blank=True
    )
    status = models.CharField(max_length=20,choices=NEWS_STATUS)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural="News"
        verbose_name="News"
