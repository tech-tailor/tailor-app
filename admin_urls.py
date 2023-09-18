from django.contrib import admin
from django.urls import path


#the built in admin module, we reverse the url to become a sub-domain host.py
urlpatterns = [
    path('', admin.site.urls),  # Use an empty string for the subdomain
]