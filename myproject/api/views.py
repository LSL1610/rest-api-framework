from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Domain
from .serializers import DomainSerializer

# Create your views here.
class DomainListView(ListAPIView):
    queryset = Domain.objects.all()
    serializer_class = DomainSerializer