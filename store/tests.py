#from django.test import TestCase

import sys
import os

print(sys.path)
project_directory = '/home/tech-tailor/python-work/tailor-app'
sys.path.append(os.path.abspath(project_directory))
print(sys.path)
from store.pillow import resize, crop, blur, imageinfo




input_path = '/home/tech-tailor/python-work/tailor-app/store/static/store/media/header2.jpg'
output_path = '/home/tech-tailor/python-work/tailor-app/store/static/store/media/header_office.png'
max_width = 60
max_height = 10


#resize(input_path, max_width, max_height, output_path)
crop(input_path, 20, 70, 570, 320, output_path)
blur(output_path, output_path)
imageinfo(input_path)
imageinfo(output_path)
    
 
    

