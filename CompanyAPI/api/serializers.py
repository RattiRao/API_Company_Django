from rest_framework import serializers
from api.models import CompanyModel, EmployeeModel
# Company Serializer


class CompanySerializer(serializers.HyperlinkedModelSerializer):
    company_id = serializers.ReadOnlyField()

    class Meta:
        model = CompanyModel
        fields = '__all__'

# Employee Serializer


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = EmployeeModel
        fields = '__all__'
