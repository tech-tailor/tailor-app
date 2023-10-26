import random
from django.shortcuts import render, redirect, get_object_or_404
from store.models import  *
from django.contrib.auth.decorators import login_required
from work.models import  Clients
from user.decorators import phone_number_required
from django.urls import reverse
from store.forms import MeasurementForm
from django.contrib.auth import get_user_model


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
def myprofile2(request):
    context = {}
    return render(request, 'store/myprofile2.html', context)


@login_required
def myprofile(request, phone_number=None):
    context = {}
    client_phone_number2 = []
    client_phone_number = []
    try:
        client2 = User_Uploaded_Measurement.objects.get(phone_number=phone_number)
        client_phone_number2 = client2.phone_number
    except Exception as e:
        pass
    try:
        clients = Clients.objects.get(phone_number=phone_number)
        client_phone_number = clients.phone_number
    except Exception as e:
        pass
    
    context = {
        'client_phone_number':client_phone_number,
        'client_phone_number2':client_phone_number2
    }
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
def clientdetails(request, phone_number=None):
  
    try:
        client = Clients.objects.get(phone_number=phone_number)
        client_phone_number = client.phone_number
        print('start')
        if not client_phone_number == request.user.phone_number:
            print(f' not equal oo {client_phone_number}')
            return redirect ('store_no_measurement')
        else:
            print(f'equal oo {client_phone_number}')
            context = {
                'client':client,
                'client_phone_number':client_phone_number,
            }
            return render(request, 'store/clientdetails.html', context)
            
    except Exception as e:
        print(f'error: {e}')
        return redirect('store_no_measurement')
    
    
    
@login_required
@phone_number_required
def user_entered_measurement(request, phone_number=None):
    try:
        client2 = User_Uploaded_Measurement.objects.get(phone_number=phone_number)
        client_phone_number2 = client2.phone_number
        print('start')
        if not client_phone_number2 == request.user.phone_number:
            print(f' not equal oo2 {client_phone_number2}')
            return redirect ('store_no_measurement')
        else:
            print(f'equal oo {client_phone_number2}')
            context = {
                'client2':client2,
                'client_phone_number2':client_phone_number2,
            }
            return render(request, 'store/clientdetails.html', context)
            
    except Exception as e:
        print(f'error2: {e}')
        return redirect('store_no_measurement')
    
    
   
@login_required
@phone_number_required 
def no_measurement(request):
    context = {}
    return render(request, 'store/no_measurement.html', context)

@login_required
@phone_number_required
def upload_measurement(request):
    if request.method == "POST":
        form = MeasurementForm(request.POST)
        if form.is_valid():
            phone_number = request.user.phone_number
            username = request.user.username
            top_lenght = form.cleaned_data['top_lenght']
            shoulder = form.cleaned_data['shoulder']
            cuff = form.cleaned_data['cuff']
            neck = form.cleaned_data['neck']
            
            try:
                if request.user.is_authenticated:
                    User_Uploaded_Measurement.objects.update_or_create(
                        user=request.user,
                        defaults={
                            'top_lenght': top_lenght,
                            'neck': neck,
                            'shoulder': shoulder,
                            'cuff': cuff,
                            'phone_number' : phone_number,
                            'measurement_name': username,
                            
                        }
                    )
                    print('success')
                else:
                    pass
            except Exception as e:
                print(f'error: {e}')
    else:
        pass
        form = MeasurementForm()
    return render(request, 'store/upload_measurement.html', {'form': form})                
    
