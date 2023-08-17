from django import forms
from django.contrib import admin
from django.core.exceptions import ValidationError

# Register your models here.
from .models import *


class JobAdmin(admin.ModelAdmin):
    list_display = ['name']
    orderin = ['-id']

class WorkersAdmin(admin.ModelAdmin):
    list_display = ['name', 'user' ]


class ClientAdmin(admin.ModelAdmin):
    def clean(self):
        name = self.cleaned_data['name']
        measurement = self.cleaned_data["measurement"]
        if measurement != name:
            raise ValidationError("Client's name must be same with the measurement name")
    


admin.site.register(ClientMeasurements)
admin.site.register(Clients, ClientAdmin)
admin.site.register(Workers, WorkersAdmin)
admin.site.register(Jobs, JobAdmin)
admin.site.register(Job_operation)
admin.site.register(Job_payment)
admin.site.register(Job_delivery)