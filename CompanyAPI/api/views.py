from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from api.models import CompanyModel, EmployeeModel
from api.serializers import CompanySerializer, EmployeeSerializer

# Create your views here.

# Company View Set


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = CompanyModel.objects.all()
    serializer_class = CompanySerializer

    # company/{company_id}/employees
    @action(detail=True, methods=['get'])
    def employees(self, request, pk=None):
        try:
            company = CompanyModel.objects.get(pk=pk)
            employees = EmployeeModel.objects.filter(company=company)
            emp_serializer_obj = EmployeeSerializer(
                employees, many=True, context={'request': request})
            return Response(emp_serializer_obj.data)
        except Exception as e:
            return Response({
                'message': str(e) 
            })

# Employee View Set


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = EmployeeModel.objects.all()
    serializer_class = EmployeeSerializer
