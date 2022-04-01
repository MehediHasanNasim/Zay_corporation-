from django.shortcuts import render
from rest_framework import viewsets
from .models import Details
from .serializers import DetailsSerializer

from django.http import HttpResponse


class DetailsView(viewsets.ModelViewSet):
    queryset = Details.objects.all()
    serializer_class = DetailsSerializer

