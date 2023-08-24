from django.conf import settings
from django_hosts import patterns, host

host_patterns = patterns('',
    host(r'www', settings.ROOT_URLCONF, name='default'),
    host(r'work', 'core.urls', name='work'),
)