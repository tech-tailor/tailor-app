# Generated by Django 4.2.4 on 2023-08-05 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, null=True)),
                ('email', models.CharField(max_length=50, null=True)),
                ('phone_number', models.IntegerField(blank=True, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('sex', models.CharField(choices=[('MALE', 'Male'), ('FEMALE', 'Female')], max_length=50)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('client_note', models.TextField(blank=True, null=True)),
                ('size', models.CharField(choices=[('S', 'Small'), ('M', 'Medium')], default='M', max_length=1)),
                ('top_lenght', models.CharField(blank=True, max_length=15, null=True)),
                ('shoulder', models.CharField(blank=True, max_length=15, null=True)),
                ('Round_chest', models.CharField(blank=True, max_length=15, null=True)),
                ('trouser_lenght', models.CharField(blank=True, max_length=15, null=True)),
                ('cap', models.CharField(blank=True, max_length=15, null=True)),
            ],
        ),
    ]