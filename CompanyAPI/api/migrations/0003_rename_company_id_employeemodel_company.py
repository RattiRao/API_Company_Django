# Generated by Django 4.2.4 on 2023-08-26 09:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_employeemodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employeemodel',
            old_name='company_id',
            new_name='company',
        ),
    ]
