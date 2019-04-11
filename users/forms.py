from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    username = forms.CharField(label="사용자 이름", widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))
    password1 = forms.CharField(label="비밀번호", widget=forms.PasswordInput(attrs={
        'class': 'form-control',
    }))
    password2 = forms.CharField(label="비밀번호 확인", widget=forms.PasswordInput(attrs={
        'class': 'form-control',
    }))

    class Meta:
        model = User
        fields = ("username",)

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
