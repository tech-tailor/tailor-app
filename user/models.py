from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import Group


# Create your models here.
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    phone_number = PhoneNumberField(unique=True,blank=True, null=True)
    verified = models.BooleanField(default=False)
    verify_code = models.CharField(max_length=6, unique=True, blank=True, null=True)
    
    
    #USERNAME_FIELD = 'phone_number'

    def __str__(self):
        return self.username
    


class CustomUserGroup(Group):
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Custom User Group'
        verbose_name_plural = 'Custom User Groups'

