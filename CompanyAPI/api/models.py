from django.db import models

# Create your models here.

# Company Model


class CompanyModel(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    about = models.TextField()
    type = models.CharField(
        max_length=100,
        choices=(("IT Company", "IT Company"),
                 ("Non IT Company", "Non IT Company")),
    )
    created_at = models.DateTimeField(auto_now=True)
    isActive = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name

# Employee Model


class EmployeeModel(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    designation = models.CharField(max_length=50,
                                   choices=(
                                       ('Level 1', 'Associate'),
                                       ('Level 2', 'Senior Associate'),
                                       ('Manager', 'Manager'),
                                       ('Senior Manager', 'Senior Manager'),
                                       ('Directo r', 'Director')
                                   ))
    company = models.ForeignKey(CompanyModel, on_delete=models.CASCADE)
