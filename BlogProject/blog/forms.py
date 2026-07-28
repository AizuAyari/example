from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Article


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]


class ArticleForm(forms.ModelForm):
    keywords = forms.CharField(
        required=False,
        help_text="カンマ区切りで入力してください（例: django, htmx）",
    )

    class Meta:
        model = Article
        fields = ["title", "content"]
