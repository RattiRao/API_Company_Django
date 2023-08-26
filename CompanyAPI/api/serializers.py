from rest_framework import serializers
from api.models import CompanyModel
# Company Serializer
class CompanySerializer(serializers.HyperlinkedModelSerializer):
    company_id = serializers.ReadOnlyField()
    class Meta:
        model = CompanyModel
        fields = '__all__'