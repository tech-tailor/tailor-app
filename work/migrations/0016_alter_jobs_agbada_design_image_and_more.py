# Generated by Django 4.2.4 on 2023-09-19 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0015_rename_name_jobs_job_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='agbada_design_image',
            field=models.ImageField(blank=True, null=True, upload_to='work/jobs/agbada_designs'),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='cap_design_image',
            field=models.ImageField(blank=True, null=True, upload_to='work/jobs/cap_designs'),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='cap_fabric_image',
            field=models.ImageField(blank=True, null=True, upload_to='work/jobs/cap_fabric'),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='fabric_image_1',
            field=models.ImageField(blank=True, null=True, upload_to='work/jobs/fabric_images'),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='fabric_image_2',
            field=models.ImageField(blank=True, null=True, upload_to='work/jobs/fabric_images'),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='top_design_image_1',
            field=models.ImageField(blank=True, null=True, upload_to='work/jobs/top_designs'),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='top_design_image_2',
            field=models.ImageField(blank=True, null=True, upload_to='work/jobs/top_designs'),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='trouser_design_image',
            field=models.ImageField(blank=True, null=True, upload_to='work/jobs/trouser_designs'),
        ),
    ]
