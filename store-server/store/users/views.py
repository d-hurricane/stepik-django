from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect as redirect
from django.contrib import auth
from users.forms import UserLoginForm, UserRegistrationForm


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
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('users:login'))
    else:
        form = UserRegistrationForm()
    context = {
        'title': 'Store - Регистрация',
        'form': form,
    }
    return render(request, 'users/register.html', context)
