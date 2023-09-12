# Generated by Django 4.2.4 on 2023-08-05 15:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0003_rename_name_clients_client_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clients',
            old_name='client_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='job_delivery',
            old_name='job_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='job_operation',
            old_name='job_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='job_payment',
            old_name='job_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='jobs',
            old_name='job_name',
            new_name='name',
        ),
    ]
