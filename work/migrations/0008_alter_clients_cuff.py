# Generated by Django 4.2.5 on 2023-11-01 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0007_alter_worker_profile_sex'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clients',
            name='cuff',
            field=models.CharField(default='', max_length=15),
        ),
    ]
