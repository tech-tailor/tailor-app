# Generated by Django 4.2.4 on 2023-08-12 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_rename_client_name_clients_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('Mr', 'Mr'), ('Mrs', 'Yes')], default='Mr', max_length=10)),
            ],
        ),
        migrations.AlterField(
            model_name='jobs',
            name='agbada_design_image',
            field=models.ImageField(blank=True, null=True, upload_to='agbada_designs'),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='cap_design_image',
            field=models.ImageField(blank=True, null=True, upload_to='cap_designs'),
        ),
    ]