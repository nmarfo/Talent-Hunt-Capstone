from django import forms
from .models import TalentProfile, TalentImage


class TalentProfileForm(forms.ModelForm):
    class Meta:
        model = TalentProfile
        fields = [
            'full_name',
            'date_of_birth',
            'gender',
            'country',
            'location',
            'category',
            'experience_level',
            'height_cm',
            'weight_kg',
            'bio',
            'skills',
            'achievements',
            'social_link',
            'image',
            'video_link',
        ]
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'bio': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Tell us about yourself...'}),
            'skills': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Example: Singing, Acting, Football'}),
            'achievements': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Awards, performances, competitions...'}),
            'social_link': forms.URLInput(attrs={'placeholder': 'Instagram, YouTube, portfolio, etc.'}),
            'video_link': forms.URLInput(attrs={'placeholder': 'Paste YouTube video link'}),
        }


class ContactTalentForm(forms.Form):
    sender_name = forms.CharField(max_length=100)
    sender_email = forms.EmailField()
    subject = forms.CharField(max_length=150)
    message = forms.CharField(widget=forms.Textarea)


class TalentImageForm(forms.ModelForm):
    class Meta:
        model = TalentImage
        fields = ['image', 'caption']