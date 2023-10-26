
import os
import sys
import django
project_directory = '/home/tech-tailor/python-work/tailor-app'
sys.path.append(os.path.abspath(project_directory))
django.setup()

from django.db.models import Count
from work.models import Clients  # Replace 'yourapp' with your actual app name
from django.db.models import F, Max
from django.db import transaction



# Query to identify duplicate client names and count their occurrences
duplicate_clients = Clients.objects.values('measurement_name').annotate(name_count=Count('measurement_name')).filter(name_count__gt=1)

# 'duplicate_clients' now contains a queryset with client names that have duplicates and the count of their occurrences.

for duplicate in duplicate_clients:
    client_name = duplicate['measurement_name']
    count = duplicate['name_count']
    print(f"Client name: {client_name}, Duplicates: {count}")
    # You can choose how to handle the duplicates based on your requirements.


# Get a distinct list of 'measurement_name' to keep one entry for each unique name.
distinct_names = Clients.objects.values('measurement_name').annotate(count=Count('measurement_name')).filter(count__gt=1)

# Iterate through the distinct measurement names and keep one entry for each name.
for entry in distinct_names:
    measurement_name = entry['measurement_name']

    # Get the IDs of all entries with the same 'measurement_name' except for the first one.
    ids_to_delete = Clients.objects.filter(measurement_name=measurement_name).exclude(id=F('pk')).values_list('id', flat=True)
    print(ids_to_delete)
    
    # Delete the duplicates except for the first one.
    Clients.objects.filter(id__in=ids_to_delete).delete()
    
# Commit the changes to the database
from django.db import transaction
transaction.commit()
print('successful')


