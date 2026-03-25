from django.db import models
from django.conf import settings


class TalentProfile(models.Model):
    CATEGORY_CHOICES = (
        ('football', 'Football'),
        ('basketball', 'Basketball'),
        ('music', 'Music'),
        ('dance', 'Dance'),
        ('acting', 'Acting'),
        ('other', 'Other'),
    )

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    full_name = models.CharField(max_length=100)
    age = models.IntegerField()
    location = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    bio = models.TextField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.full_name