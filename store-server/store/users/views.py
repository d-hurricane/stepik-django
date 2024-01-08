from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect as redirect
from django.contrib import auth
from users.forms import UserLoginForm


def login(request):
    if request.method == 'POST':
        data = request.POST
        form = UserLoginForm(data=data)
        if form.is_valid():
            username, password = data['username'], data['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return redirect(reverse('index'))
    else:
        form = UserLoginForm()
    context = {
        'title': 'Store - Авторизация',
        'form': form,
    }
    return render(request, 'users/login.html', context)


def register(request):
    context = {
        'title': 'Store - Регистрация',
    }
    return render(request, 'users/register.html', context)
