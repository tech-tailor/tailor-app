import random
from django.shortcuts import render, redirect, get_object_or_404
from store.models import  *
from django.contrib.auth.decorators import login_required
from work.models import  Clients
from user.decorators import phone_number_required
from django.urls import reverse



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

@login_required
def myprofile(request):
    context = {}
    return render(request, 'store/myprofile.html', context)



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

@login_required
@phone_number_required
def clientdetails(request, phone_number):
    
    try:
        client = Clients.objects.get(phone_number=phone_number)
        client_phone_number = client.phone_number
        if  not client_phone_number == request.user.phone_number:
            print(f' not equal oo {client_phone_number}')
            return redirect ('store_no_measurement')
        else:
            print(f'equal oo {client_phone_number}')
            context = {
                'clients':client,
                'client_phone_number':client_phone_number,
            }
            return render(request, 'store/clientdetails.html', context)
            
    except Clients.DoesNotExist:
        return redirect('store_no_measurement')
    
    except Clients.MultipleObjectsReturned:
        return redirect('store_no_measurement')

@login_required
@phone_number_required 
def no_measurement(request):
    context = {}
    return render(request, 'store/no_measurement.html', context)
    