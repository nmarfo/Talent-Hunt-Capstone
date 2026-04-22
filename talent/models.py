from datetime import date
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

    EXPERIENCE_CHOICES = (
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('professional', 'Professional'),
    )

    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    )

    COUNTRY_CHOICES = (
        ('ghana', 'Ghana'),
        ('nigeria', 'Nigeria'),
        ('kenya', 'Kenya'),
        ('south_africa', 'South Africa'),
        ('usa', 'United States'),
        ('uk', 'United Kingdom'),
        ('canada', 'Canada'),
        ('other', 'Other'),
    )

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    full_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, blank=True)
    country = models.CharField(max_length=50, choices=COUNTRY_CHOICES, blank=True)
    location = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    experience_level = models.CharField(max_length=20, choices=EXPERIENCE_CHOICES, blank=True)

    height_cm = models.PositiveIntegerField(null=True, blank=True)
    weight_kg = models.PositiveIntegerField(null=True, blank=True)

    bio = models.TextField()
    skills = models.TextField(blank=True, help_text="Example: Singing, Acting, Football")
    achievements = models.TextField(blank=True, help_text="Awards, competitions, performances, etc.")
    social_link = models.URLField(blank=True, null=True)

    image = models.ImageField(upload_to='talent_images/', null=True, blank=True)
    video_link = models.URLField(blank=True, null=True)

    is_verified = models.BooleanField(default=False)
    likes = models.PositiveIntegerField(default=0)

    @property
    def age(self):
        if not self.date_of_birth:
            return None
        today = date.today()
        return today.year - self.date_of_birth.year - (
            (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day)
        )

    def __str__(self):
        return self.full_name


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