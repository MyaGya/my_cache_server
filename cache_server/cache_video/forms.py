from django import forms
from .models import User, UploadedFile, LocalUrl, TrackingUrl


class UploadForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = ['subject', 'local']


