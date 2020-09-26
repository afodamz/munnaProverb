from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.authentication import TokenAuthentication, BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *


# Create your views here.
class ProverbsViewSet(viewsets.ModelViewSet):
    serializer_class = ProverbSerializer
    queryset = Proverb.objects.all()

    authentication_classes = [TokenAuthentication, SessionAuthentication, BasicAuthentication]
    # permission_classes = (IsAuthenticated,)
    permission_classes = [IsAuthenticatedOrReadOnly,]
