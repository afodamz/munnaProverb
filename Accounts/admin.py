from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class CustomUserAdmin(UserAdmin):
    ordering = ('email',)

admin.site.register(CustomUser, CustomUserAdmin)