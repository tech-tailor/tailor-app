from django.conf import settings
from django.contrib import admin
from django_hosts import patterns, host

host_patterns = patterns('',
    host(r'www', settings.ROOT_URLCONF, name='default'), #for production enviroment
    host(r'work', 'work.urls', name='work'),   # workapp for production enviroment
    host(r'work-test', 'work.urls', name='work-test'),  # the work app for the testing enviroment
    host(r'test', 'store.urls', name='test'),   #the home url for testing enviroment
    host(r'gladmin', 'admin_urls', name='admin'), #the admin url for all the modules
    host(r'account', 'allauth.urls', name='account'), #the admin url for all the modules
)