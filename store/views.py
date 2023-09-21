from django.shortcuts import render


# Create your views here.
from .models import  *

def home(request):
    context = {}
    return render(request, 'store/home.html', context)

def product(request):
    context = {}
    return render(request, 'store/product.html', context)


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

def productpage(request):
    context = {}
    return render(request, 'store/productpage.html', context)







