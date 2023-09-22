import random
from django.shortcuts import render


# Create your views here.
from store.models import  *


def discount_percentage(products):
        percentage = []
        for product in products:
            discount = product.price - product.discount_price
            percent = discount/product.price * 100
            percentage.append(percent)
        return percentage

def home(request):
    products = Product.objects.all()
    carousels = Carousel.objects.all()
    categories = Category.objects.all()

    random_selection_products = Product.random_products()
    for product in random_selection_products:
        discount = product.price - product.discount_price
        percent = round(discount/product.price * 100)
        product.discount_percentage = percent

    feature_products = Product.featureproducts()
    for product in feature_products:
        discount = product.price - product.discount_price
        percent = round(discount/product.price * 100)
        product.discount_percentage = percent
    context = {
        'products':products,
        'carousels':carousels,
        'categories':categories,
        'random_selection_products':random_selection_products,
        'discount':discount,
        'feature_products':feature_products
    }
    return render(request, 'store/home.html', context)

def productpage(request, product_id):
    products = Product.objects.get(product_id=product_id)
    #for product in products:
     #   discount = product.price - product.discount_price
      #  percent = round(discount/product.price * 100)
       # product.discount_percentage = percent
    image_1_url = products.image_url('image_1')
    image_2_url = products.image_url('image_2')
    image_3_url = products.image_url('image_3')
    context = {
        'products':products,
        'image_1_url':image_1_url,
        'image_2_url':image_2_url,
        'image_3_url':image_3_url,
    }
    return render(request, 'store/productpage.html', context)


def login(request):
    context = {}
    return render(request, 'store/login.html', context)

def logout(request):
    context = {}
    return render(request, 'store/logout.html', context)

def register(request):
    context = {}
    return render(request, 'store/register.html', context)


def searchpage(request,):
    context = {}
    return render(request, 'store/searchpage.html', context)

def product(request):
    products = Product.objects.all()
    for product in products:
        discount = product.price - product.discount_price
        percent = round(discount/product.price * 100)
        product.discount_percentage = percent
    context = {
        'products':products
    }
    return render(request, 'store/product.html', context)







