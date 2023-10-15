from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import Group


# Create your models here.
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    phone_number = PhoneNumberField(default='+234',
        blank=True,
        null=True,
        help_text='Enter a valid phone number in E.164 format.')
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.username
    


class CustomUserGroup(Group):
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Custom User Group'
        verbose_name_plural = 'Custom User Groups'

