from django import forms
from .models import Profile
from django.contrib.auth.models import User

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar','nike']
        widgets = {'avatar':forms.ClearableFileInput(attrs={'class':'image_upload_but'})}
