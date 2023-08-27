from django.contrib import admin
from api.models import CompanyModel, EmployeeModel

# Register your models here.
admin.site.register(CompanyModel)
admin.site.register(EmployeeModel)
