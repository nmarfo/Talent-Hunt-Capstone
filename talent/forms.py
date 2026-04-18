from django import forms
from .models import TalentProfile, TalentImage


class TalentProfileForm(forms.ModelForm):
    class Meta:
        model = TalentProfile
        fields = ['full_name', 'age', 'location', 'category', 'bio', 'image', 'video_link']
        widgets = {
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