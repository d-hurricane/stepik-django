from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from users.forms import (
    UserLoginForm,
    UserRegistrationForm,
    UserProfileForm,
)
from products.views import (
    Basket,
)


class UserLoginView(LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm
    extra_context = {'title': 'Store - Авторизация'}


class UserRegistrationView(SuccessMessageMixin, CreateView):
    template_name = 'users/register.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('users:login')
    extra_context = {'title': 'Store - Регистрация'}
    success_message = 'Вы успешно зарегистрированы'


class UserProfileView(LoginRequiredMixin, UpdateView):
    template_name = 'users/profile.html'
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')
    extra_context = {'title': 'Store - Профиль'}

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['basket'] = Basket.objects.filter(user=self.object)
        return context
