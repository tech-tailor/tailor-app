# Generated by Django 4.2.5 on 2023-10-23 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0004_worker_profile_verified'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='worker_profile',
            name='verified',
        ),
        migrations.AddField(
            model_name='worker_profile',
            name='next_of_kin',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]