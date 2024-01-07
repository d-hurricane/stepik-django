from django.shortcuts import render


def login(request):
    context = {
        'title': 'Store - Авторизация',
    }
    return render(request, 'users/login.html', context)


def register(request):
    context = {
        'title': 'Store - Регистрация',
    }
    return render(request, 'users/register.html', context)
