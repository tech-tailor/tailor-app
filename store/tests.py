#from django.test import TestCase

import sys
import os

print(sys.path)
project_directory = '/home/tech-tailor/python-work/tailor-app'
sys.path.append(os.path.abspath(project_directory))
print(sys.path)
from store.pillow import recrop, resize, myresize, crop, blur, imageinfo




input_path = '/home/tech-tailor/python-work/tailor-app/store/static/store/media/IMG_0349.JPG'
output_path = '/home/tech-tailor/python-work/tailor-app/store/static/store/media/header_office.png'
max_width = 700
max_height = 800


resize(input_path, max_width, max_height)
crop(input_path, 700, 800)
#(output_path, output_path)
#imageinfo(input_path)
#imageinfo(output_path)
    
 

