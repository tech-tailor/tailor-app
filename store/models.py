import random
from django.db import models
import uuid
from django.templatetags.static import static
from django.db.models import F


class Size(models.Model):
    name = models.CharField(max_length=20, null=True, blank=True, unique=True)
    label = models.CharField(max_length=20, null=True, blank=True, unique=True)

    def __str__(self):
        return str(self.name)

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return str(self.name)

class Category(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True, unique=True)
    image = models.ImageField(blank=True, null=True, upload_to='store/category/images')
    description = models.TextField(max_length=250, null=True, blank=True,)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return str(self.name)
    
    '''return a placeholder image when no image is uploaded'''
    def imageurl(self): 
        try:
            image_field = self.image
            return image_field.url
        except (AttributeError, ValueError):
            #no_image_available_url = static('work/media/no_image_available.png')
            return 

class Carousel(models.Model):
    title = models.TextField(max_length=250, null=True, blank=True, unique=True)
    text = models.TextField(max_length=250, null=True, blank=True, unique=True)
    image = models.ImageField(blank=True, null=True, upload_to='store/carousel/images')
    def __str__(self):
        return str(self.title)
    
    '''return a placeholder image when no image is uploaded'''
    def imageurl(self): 
        try:
            image_field = self.image
            return image_field.url
        except (AttributeError, ValueError):
            no_image_available_url = static('work/media/no_image_available.png')
            return 



class Product(models.Model):
    product_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(max_length=250, null=True, blank=True,)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)
    size = models.ManyToManyField(Size, blank=True)
    delivery = models.CharField(max_length=100)
    stock_quantity = models.PositiveIntegerField(default=0)
    image_1 = models.ImageField(blank=True, null=True, upload_to='store/Product/images')
    image_2 = models.ImageField(blank=True, null=True, upload_to='store/Product/images')
    image_3 = models.ImageField(blank=True, null=True, upload_to='store/Product/images')
    date_uploaded = models.DateTimeField(auto_now_add=True)  # Set on creation
    date_updated = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return str(self.name)
    
    @classmethod
    def random_products(cls):
        try:
            all_products = cls.objects.all()
            products = random.sample(list(all_products), 5)
            return products
        except ValueError:
            return all_products

    #return a placeholder image when no image is uploaded
    def imageurl(self): 
        try:
            image_field = self.image_1
            return image_field.url
        except (AttributeError, ValueError):
            #no_image_available_url = static('work/media/no_image_available.png')
            return 
        

    def image_url(self, field_name): 
        try:
            image_field = getattr(self, field_name)
            return image_field.url
        except (AttributeError, ValueError):
            #no_image_available_url = static('work/media/no_image_available.png')
            return ''
        
    #random products to display in the home    
    @classmethod
    def featureproducts(cls):
        try:
            all_products = cls.objects.all()
            #12 feature products maximum in the home page
            products = random.sample(list(all_products), 12) 
            return products
        except ValueError:
            return all_products

