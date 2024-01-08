from django import forms
from django.contrib.auth.forms import AuthenticationForm

import users.models as models


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = models.User
        fields = ('username', 'password')

    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4',
        'placeholder': 'Введите имя пользователя',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4',
        'placeholder': 'Введите пароль',
    }))
