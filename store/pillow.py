
import os
import sys

#print(sys.path)
from PIL import Image, ImageFilter




def resize(image, max_width, max_height, output_path):
    img =Image.open(image)
    print('start')
    
    original_width, original_height = img.size
    image_bytes = img.tobytes()
    img_size = len(image_bytes)/1000

    # Calculate the new dimensions while maintaining the aspect ratio
    if original_width > max_width or original_height > max_height:
        width_ratio = max_width / original_width
        height_ratio = max_height / original_height
        ratio = min(width_ratio, height_ratio)

        new_width = int(original_width * ratio)
        new_height = int(original_height * ratio)

        # Resize the image with the calculated dimensions
        img = img.resize((new_width, new_height), Image.LANCZOS)
        image_bytes = img.tobytes()
        new_img_size = len(image_bytes)/1000
        
        img.save(output_path)
        print('Succesfully resize L{} by W{} of S{}  TO L{} by W{} S{}'.format( original_height,original_width, img_size, max_height, max_width, new_img_size))
    else:
        print('You cannot resize L{} by W{} to L{} by W{}'.format( original_height,original_width, max_height, max_width))


def crop(image, left, upper, right, lower, output):
    with Image.open(image) as img:
        
        
        print(img.size)
    
        crop_img = img.crop((left, upper, right, lower))
        
        print(crop_img.size)
        crop_img.save(output)
        print('successfully cropped the image')
        
def blur(image, output):
    with Image.open(image) as img:
        
        blur_img = img.filter(ImageFilter.GaussianBlur(radius=1))
        blur_img.save(output)
        print('successfully blurred the image')
        
def imageinfo(image):
    with Image.open(image) as img:
        
        height, width = img.size
        image_size = int(os.path.getsize(image) / 1024.0)
        
        print('Image Info, Height= {}pixel, Width= {}pixel, Size={}kb'.format(height, width, image_size ))
        