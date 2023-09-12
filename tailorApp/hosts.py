from django.conf import settings
from django.contrib import admin
from django_hosts import patterns, host

host_patterns = patterns('',
    host(r'www', settings.ROOT_URLCONF, name='default'),
    host(r'work', 'work.urls', name='work'),
    host(r'my-admin', admin.site.urls, name='admin'),
    host(r'client', 'client.urls', name='client'),
)