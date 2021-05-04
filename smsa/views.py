from rest_framework import viewsets
from django.shortcuts import render
from .serializers import HeroSerializer
from .models import Hero
import requests
import json


class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer

def index(request):
    response = requests.get('http://127.0.0.1:8000/api/heroes/')
    name = response.json()
    return render(request, 'index.html', {
        'data': name}
    )