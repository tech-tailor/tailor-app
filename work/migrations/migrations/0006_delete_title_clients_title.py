# Generated by Django 4.2.4 on 2023-08-12 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0005_title_alter_jobs_agbada_design_image_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Title',
        ),
        migrations.AddField(
            model_name='clients',
            name='title',
            field=models.CharField(choices=[('Mr', 'Mr'), ('Mrs', 'Yes')], default='Mr', max_length=10),
        ),
    ]
