from django.contrib import admin
from store.models import *
from django.conf import settings
from django.contrib.admin.views.decorators import staff_member_required
from store.pillow import crop, resize
from PIL import Image
from store.forms import CarouselForm, ProductForm



admin.site.login = staff_member_required(
    admin.site.login, login_url=settings.LOGIN_URL
)
    
    
class CarouselAdmin(admin.ModelAdmin):
    form = CarouselForm
    def save_model(self, request, obj, form, change):
        # Call the parent class's save_model method
        super().save_model(request, obj, form, change)
        
        
        width = 500
        height = 200

        # Check if there is an image file to process
        if 'image' in form.changed_data:
            new_image = form.cleaned_data.get('image')
            
            if new_image:
                with Image.open(obj.image.path) as image:
                    original_width, original_height = image.size
                    if original_width >= width and original_height >= height:
                        #Crop the image
                        crop(obj.image.path, width, height)
                        obj.image = new_image    
                    else:
                        obj.image.delete()
                    
            else:
                obj.image.delete()
                

class ProductAdmin(admin.ModelAdmin):
    form = ProductForm

    def save_model(self, request, obj, form, change):
        # Call the parent class's save_model method
        super().save_model(request, obj, form, change)

        width = 700
        height = 800

        # Process 'image_1'
        if 'image_1' in form.changed_data:
            new_image = form.cleaned_data.get('image_1')
            current_image = obj.image_1

            if current_image and current_image.path:
                with Image.open(current_image.path) as image:
                    original_width, original_height = image.size
                    if original_width >= width and original_height >= height:
                        # Crop the image
                        resize(current_image.path, 1000, 800)
                        crop(current_image.path, width, height)
                        obj.image_1 = new_image
                    else:
                        # Delete the existing 'image_1'
                        current_image.delete()
                if not new_image:
                    obj.image_1 = None

        # Process 'image_2'
        if 'image_2' in form.changed_data:
            new_image = form.cleaned_data.get('image_2')
            current_image = obj.image_2

            if current_image and current_image.path:
                with Image.open(current_image.path) as image:
                    original_width, original_height = image.size
                    if original_width >= width and original_height >= height:
                        # Crop the image
                        resize(current_image.path, 1000, 800)
                        crop(current_image.path, width, height)
                        obj.image_2 = new_image
                    else:
                        # Delete the existing 'image_2'
                        current_image.delete()
                if not new_image:
                    obj.image_2 = None
                    
        # Process 'image_2'
        if 'image_3' in form.changed_data:
            new_image = form.cleaned_data.get('image_3')
            current_image = obj.image_3

            if current_image and current_image.path:
                with Image.open(current_image.path) as image:
                    original_width, original_height = image.size
                    if original_width >= width and original_height >= height:
                        # Crop the image
                        resize(current_image.path, 1000, 800)
                        crop(current_image.path, width, height)
                        obj.image_3 = new_image
                    else:
                        # Delete the existing 'image_3'
                        current_image.delete()
                if not new_image:
                    obj.image_3 = None
                
       

admin.site.register(Tag)
admin.site.register(Size)
admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(UserProfile)
admin.site.register(TemporaryPhoneNumber)
admin.site.register(Carousel, CarouselAdmin)
admin.site.register(User_Uploaded_Measurement)
