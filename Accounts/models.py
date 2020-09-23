from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from .manager import *

from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail


from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives

# Create your models here.
class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email_address'), unique=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = CustomUserManager()

    def __str__(self):
        return self.email
