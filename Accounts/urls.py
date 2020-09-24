from django.urls import path, include

from allauth.account.views import confirm_email
from .views import *

from rest_auth.views import PasswordResetConfirmView

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', CustomRegisterView.as_view()),

    path('registration/', RegisterView.as_view(), name='registration'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('password-update/', ChangePasswordView.as_view(), name='password-update'),

    path('request-resent-email/', RequestPasswordResetEmail.as_view(), name='request-reset-email'),
    path('password_reset/<uidb64>/<token>/', PasswordTokenCheckAPI.as_view(), name='reset_password_confirm'),
    path('password-reset-complete/', SetNewPasswordAPIView.as_view(), name='password-reset-complete'),
]