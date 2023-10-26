#from django.test import TestCase

import sys
import os

print(sys.path)
project_directory = '/home/tech-tailor/python-work/tailor-app'
sys.path.append(os.path.abspath(project_directory))
print(sys.path)
from store.pillow import recrop, resize, myresize, crop, blur, imageinfo
from PIL import Image



input_path = '/home/tech-tailor/python-work/tailor-app/store/static/store/media/blukaf.jpg'
output_path = '/home/tech-tailor/python-work/tailor-app/store/static/store/media/header_office.png'
max_width = 1050
max_height = 1200

with Image.open(input_path) as img:
    
    width, height = img.size
    ratio = width / height
    
    #for 6 by
    if ratio < 0.75:
        resize(input_path, max_width, max_height)
        crop(input_path, 700, 800)
        
    elif ratio > 0.75:
        resize(input_path, 700, 800)
        


    
    #(output_path, output_path)
    #imageinfo(input_path)
    #imageinfo(output_path)
        
 

