from django.contrib import admin

# Register your models here.
from .models import *



    


admin.site.register(ClientMeasurements)
admin.site.register(Clients)
admin.site.register(Workers)
admin.site.register(Jobs)
admin.site.register(Job_operation)
admin.site.register(Job_payment)
admin.site.register(Job_delivery)