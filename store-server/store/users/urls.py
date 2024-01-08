import users.views as users
from django.urls import path

app_name = 'users'

urlpatterns = [
    path('login/', users.login, name='login'),
    path('register/', users.register, name='register'),
    path('profile/', users.profile, name='profile'),
    path('logout/', users.logout, name='logout'),
]
