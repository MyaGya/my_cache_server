from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import cache_video.models as cache

class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일")

    class Meta:
        model = User
        fields = ("username", "email")

class VideoForm(UserCreationForm):
    class Meta:
        model = cache.LocalUrl
        fields = ("url", "local")

