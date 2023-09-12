# Generated by Django 4.2.4 on 2023-09-12 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0005_alter_jobs_fabric_image_1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='agbada_design_image',
            field=models.ImageField(blank=True, null=True, upload_to='work/agbada_designs'),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='cap_design_image',
            field=models.ImageField(blank=True, null=True, upload_to='work/cap_designs'),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='cap_fabric_image',
            field=models.ImageField(blank=True, null=True, upload_to='work/cap_fabric'),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='top_design_image_1',
            field=models.ImageField(blank=True, null=True, upload_to='work/top_designs'),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='top_design_image_2',
            field=models.ImageField(blank=True, null=True, upload_to='work/top_designs'),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='trouser_design_image',
            field=models.ImageField(blank=True, null=True, upload_to='work/trouser_designs'),
        ),
    ]
