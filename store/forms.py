from PIL import Image
from django import forms
from django.core.exceptions import ValidationError
from .models import Carousel, Product

# make sure only images of W500 and H200 or above is saved in the carousel
#if the image is greater the CarouselModelAdmin class will call crop to trim it
class CarouselForm(forms.ModelForm):
    class Meta:
        model = Carousel
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        new_image = cleaned_data.get('image')
        width = 500
        height = 200

        if new_image:
            with Image.open(new_image) as image:
                original_width, original_height = image.size
                if original_width < width or original_height < height:
                    raise ValidationError("The image is smaller than the desired dimensions. The image must be W500 and H250 or greater")

        return cleaned_data
    
    
    
# make sure only images of W700 and H800 or above is saved in the carousel
#if the image is greater the ProductAdmin class will call crop to trim it
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        width = 700
        height = 800

        image_fields = ['image_1', 'image_2', 'image_3']

        for field_name in image_fields:
            new_image = cleaned_data.get(field_name)

            if new_image:
                with Image.open(new_image) as image:
                    original_width, original_height = image.size
                    if original_width < width or original_height < height:
                        raise ValidationError(f"The {field_name} is smaller than the desired dimensions. The image must be W700 and H800 or greater")

        return cleaned_data
