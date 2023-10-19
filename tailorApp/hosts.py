from django.conf import settings
from .settings_dev import *
from django.contrib import admin
from django_hosts import patterns, host

host_patterns = patterns('',
    host(r'www', settings.ROOT_URLCONF, name='default'), #for production enviroment
    host(r'test', settings.ROOT_URLCONF, name='test'),   #the home url for testing enviroment
    host(r'work', 'work.urls', name='work'),   # workapp for production enviroment
    host(r'work-test', 'work.urls', name='work-test'),  # the work app for the testing enviroment
    host(r'gladmin', 'admin_urls', name='admin'), #the admin url for the producton
    host(r'glaidmin-test', 'admin_urls', name='admin-test'), #the admin url for the testing enviroment
)
