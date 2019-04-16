from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms


class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(label="비밀번호", widget=forms.PasswordInput, help_text="비밀번호는 최소 8자 이상이어야 합니다.")

    class Meta:
        model = get_user_model()
        fields = ('username', 'password1', 'password2',)
