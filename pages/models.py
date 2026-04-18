from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('talent', 'Talent'),
        ('coach', 'Coach/Scout'),
    )

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='talent'
    )