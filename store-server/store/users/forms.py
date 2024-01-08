from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

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


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = models.User
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2',
        )

    first_name = forms.CharField(
        label='Имя',
        widget=forms.TextInput(attrs={
            'class': 'form-control py-4',
            'placeholder': 'Введите имя',
        }))
    last_name = forms.CharField(
        label='Фамилия',
        widget=forms.TextInput(attrs={
            'class': 'form-control py-4',
            'placeholder': 'Введите фамилию',
        }))
    username = forms.CharField(
        label='Имя пользователя',
        widget=forms.TextInput(attrs={
            'class': 'form-control py-4',
            'placeholder': 'Введите имя пользователя',
        }))
    email = forms.CharField(
        label='Адрес электронной почты',
        widget=forms.EmailInput(attrs={
            'class': 'form-control py-4',
            'placeholder': 'Введите адрес эл. почты',
        }))
    password1 = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control py-4',
            'placeholder': 'Введите пароль',
        }))
    password2 = forms.CharField(
        label='Подтверждение пароля',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control py-4',
            'placeholder': 'Подтвердите пароль',
        }))
