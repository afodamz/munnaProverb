from django.contrib import admin
from django.urls import path, include
from .views import *


from .views import ProverbsViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'', ProverbsViewSet, basename='proverbs')


urlpatterns = [

    path('', include(router.urls)),
]
