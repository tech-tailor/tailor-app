import os
import sys
import django

# Initialize Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tailorApp.settings") #Replace 'tailor.settings' with your project's settings module.

# This is to ensure that Django is properly configured and apps are loaded.


print(sys.path)
project_directory = '/home/tech-tailor/python-work/tailor-app'
sys.path.append(os.path.abspath(project_directory))
django.setup()

import pandas as pd
from work.models import Clients
from phonenumber_field.phonenumber import PhoneNumber
from phonenumber_field.phonenumber import to_python
from django.core.exceptions import ValidationError

excel_file = 'client_measurement.xlsx'
sheet_name = 'Sheet1'
df = pd.read_excel(excel_file, sheet_name)

try:
    for index, row in df.iterrows():
        phone_number = row['Phone Number']
        
        #try:
        #   phone_number = to_python(phone_number)
        #except Exception as e:
        #   pass
        #   print(f'invalid phone Number at {index}: {phone_number}, error: {e}')
        #   continue
            
        client = Clients(
            measurement_name = row['Client Name'],
            top_lenght = row['Lenght'],
            shoulder = row['Shoulder'],
            #phone_number = phone_number,
            client_note = row['Client Note'],
            Round_chest = row['Round Chest'],
            sleeve_lenght = row['Sleeve Lenght'],
            neck = row['Neck'],
            round_arm  = row['Round Arm'],
            arm_hole = row['Arm Hole'],
            front_chest = row['Front Chest'],
            back_chest = row['Back Chest'],
            cuff = row['Cuff'],
            short_sleeve_width = row['Short Sleeve Width'],
            three_quarter_width = row['3Quarter  Width'],
            long_sleeve_width = row['Long Sleeve Width'],
            trouser_lenght = row['Long Sleeve Width'],
            waist = row['Waist'],
            lap = row['Lap'],
            knee = row['Knee'],
            calf = row['Calf'],
            ankle = row['Ankle'],
            BR = row['BR'],
            RBR = row['RRB'],
            agbada_lenght = row['Agbada Lenght'],
            agbada_shoulder = row['Agbada Shoulder'],
            agbada_sleeve = row['Agbada Sleeve'],
            cap = row['Cap'],
        )
        #client.full_clean()
        client.save()
        print('client data imported successfully')
except Exception as e:
    print(f'validation error at row {index}: {phone_number} {e}')
    #continue
        
    
