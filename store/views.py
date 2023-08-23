from django.shortcuts import render

# Create your views here.
from .models import  *

def home(request):
    context = {}
    return render(request, 'store/home.html', context)
