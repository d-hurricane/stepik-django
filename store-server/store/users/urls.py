import users.views as users
from django.urls import path

app_name = 'users'

urlpatterns = [
    path('login/', users.UserLoginView.as_view(), name='login'),
    path('register/', users.UserRegistrationView.as_view(), name='register'),
    path('profile/', users.UserProfileView.as_view(), name='profile'),
    path('logout/', users.LogoutView.as_view(), name='logout'),
    path('verify/<int:user>/<uuid:code>/', users.EmailVerificationView.as_view(), name='verify'),
]
