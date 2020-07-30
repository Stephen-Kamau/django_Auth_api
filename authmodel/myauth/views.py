from django.shortcuts import render

# Create your views here.
from .serializers import myBaseUserSerializer

from rest_framework import viewsets
from .models import myBaseUser

class myBaseUserView(viewsets.ModelViewSet):
    queryset = myBaseUser.objects.all()
    serializer_class = myBaseUserSerializer
