from django import forms
from .models import TalentProfile


class TalentProfileForm(forms.ModelForm):
    class Meta:
        model = TalentProfile
        fields = ['full_name', 'age', 'location', 'category', 'bio']