from django.shortcuts import render

from .models import Pelicula
from .serializers import PeliculaSerializer

from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class PeliculaViewSet(viewsets.ModelViewSet):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Pelicula.objects.all()
    serializer_class = PeliculaSerializer