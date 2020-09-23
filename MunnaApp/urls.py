from allauth.account.views import confirm_email
from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/proverbs/', include('Proverbs.urls')),

    path('accounts/', include('Accounts.urls')),

]
