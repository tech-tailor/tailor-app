# Generated by Django 4.2.4 on 2023-09-15 17:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0009_clients_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clientmeasurements',
            old_name='client_name',
            new_name='name',
        ),
    ]
