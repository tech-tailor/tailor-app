# Generated by Django 4.2.4 on 2023-08-05 14:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_clientmeasurements_job_operation_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clients',
            old_name='name',
            new_name='client_name',
        ),
    ]
