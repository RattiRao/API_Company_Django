from django.shortcuts import render
from rest_framework import viewsets
from api.models import CompanyModel
from api.serializers import CompanySerializer

# Create your views here.

# Company View Set
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = CompanyModel.objects.all()
    serializer_class = CompanySerializer
