from django.urls import path, include

from allauth.account.views import confirm_email
from .views import *

from rest_auth.views import PasswordResetConfirmView

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', CustomRegisterView.as_view()),

    path('api-auth/', include('rest_framework.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),

    path('rest-auth/password-update/', ChangePasswordView.as_view()),

    path('rest-auth/request-resent-email/', RequestPasswordResetEmail.as_view(), name='request-reset-email'),
    path('rest-auth/password_reset/<uidb64>/<token>/', PasswordTokenCheckAPI.as_view(), name='reset_password_confirm'),
    path('rest-auth/password-reset-complete/', SetNewPasswordAPIView.as_view(), name='password-reset-complete'),
]
