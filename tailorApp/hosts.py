from django.conf import settings
from django.contrib import admin
from django_hosts import patterns, host

host_patterns = patterns('',
    host(r'www', settings.ROOT_URLCONF, name='default'), #for production enviroment
    host(r'test', 'store.urls', name='test'),   #the home url for testing enviroment
    host(r'work', 'work.urls', name='work'),   # workapp for production enviroment
    host(r'work-test', 'work.urls', name='work-test'),  # the work app for the testing enviroment
    host(r'gladmin', 'admin_urls', name='admin'), #the admin url for the production
    host(r'gladmin-test', 'admin_urls', name='admin-test'), #the admin url for the testing enviroment
    host(r'account', 'allauth.urls', name='account'), #the account url for the production
    host(r'account-test', 'allauth.urls', name='account-test'), #the acocunt url for the testing enviroment
    #host(r'client', 'client.urls', name='client'), #the client url for the production
    #host(r'client-test', 'client.urls', name='client'), #the client url for the testing enviroment
)
