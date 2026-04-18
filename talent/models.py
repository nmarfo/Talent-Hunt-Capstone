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

    # Main profile image
    image = models.ImageField(upload_to='talent_images/', null=True, blank=True)

    # Video link (YouTube, etc.)
    video_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.full_name


#  NEW MODEL FOR MULTIPLE IMAGES (GALLERY)
class TalentImage(models.Model):
    talent_profile = models.ForeignKey(
        TalentProfile,
        on_delete=models.CASCADE,
        related_name='gallery_images'
    )

    image = models.ImageField(upload_to='talent_gallery/')
    caption = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"Image for {self.talent_profile.full_name}"