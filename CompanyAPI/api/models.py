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

