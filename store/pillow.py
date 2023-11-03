
import os
import sys

#print(sys.path)
from PIL import Image, ImageFilter
from PIL import Image, ExifTags



def resize(image, max_width, max_height):
    with Image.open(image) as img:
    
        original_width, original_height = img.size
        image_bytes = img.tobytes()
        img_size = len(image_bytes) / 1000

        # Check and correct the image orientation if needed
        for orientation in ExifTags.TAGS.keys():
            if ExifTags.TAGS[orientation] == 'Orientation':
                try:
                    exif = dict(img._getexif().items())
                    if exif[orientation] == 3:
                        img = img.rotate(180, expand=False)
                    elif exif[orientation] == 6:
                        img = img.rotate(270, expand=False)
                    elif exif[orientation] == 8:
                        img = img.rotate(90, expand=False)
                except (AttributeError, KeyError, IndexError):
                    # No Exif data or Orientation tag, no rotation needed
                    pass

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
            new_img_size = len(image_bytes) / 1000

            # Save the image
            img.save(image)
            print('Successfully resized {}x{} to {}x{} (Size: {} KB -> {} KB)'.format(original_width, original_height, new_width, new_height, img_size, new_img_size))
        else:
            print('Image is smaller than the desired dimensions ({}x{})'.format(max_width, max_height))




def myresize(image, max_width, max_height):
    with Image.open(image) as img:
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
            
            img.save(image)
            print('Succesfully resize L{} by W{} of S{}  TO L{} by W{} S{}'.format( original_height,original_width, img_size, max_height, max_width, new_img_size))
        else:
            print('You cannot resize L{} by W{} to L{} by W{}'.format( original_height,original_width, max_height, max_width))


def crop(image_path, width, height):
    with Image.open(image_path) as img:
        
        img_width, img_height = img.size
        
        # Calculate the cropping box coordinates
        left = (img_width - width) / 2
        upper = (img_height - height) / 2
        right = (img_width + width) / 2
        lower = (img_height + height) / 2
        
        
        print(img.size)
    
        crop_img = img.crop((left, upper, right, lower))
        
        print(crop_img.size)
        crop_img.save(image_path)
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
        
        
def recrop(image, max_width, max_height):
    img =Image.open(image)
    print('start')
    
    original_width, original_height = img.size

    # Calculate the new dimensions while maintaining the aspect ratio
    if original_width > max_width or original_height > max_height:
        width_ratio = max_width / original_width
        height_ratio = max_height / original_height
        ratio = min(width_ratio, height_ratio)

        new_width = int(original_width * ratio)
        new_height = int(original_height * ratio)
        
        img_width, img_height = img.size
        
        # Calculate the cropping box coordinates
        left = (img_width - new_width) / 2
        upper = (img_height - new_height) / 2
        right = (img_width + new_width) / 2
        lower = (img_height + new_height) / 2
        
        
        print(img.size)
    
        crop_img = img.crop((left, upper, right, lower))
        
        print(crop_img.size)
        crop_img.save(image)
        print('successfully cropped the image')