# Generated by Django 4.2.5 on 2023-11-03 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0008_alter_clients_cuff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clients',
            name='measurement_name',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]
