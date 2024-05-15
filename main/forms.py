from django import forms
from .models import ReferralLink

class ReferralLinkForm(forms.ModelForm):
    class Meta:
        model = ReferralLink
        fields = ['text']