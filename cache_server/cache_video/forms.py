from django import forms
from .models import User, UploadedFile, LocalUrl, TrackingUrl


class UploadForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = ['subject', 'local']
        labels = {
            'subject': '제목',
            'local': '파일'
        }

class RegisterUrlForm(forms.ModelForm):
    class Meta:
        model = TrackingUrl
        fields = ['subject', 'url']
        labels = {
            'subject': '제목',
            'url': 'url'
        }
