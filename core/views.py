from django.shortcuts import get_object_or_404, render

# Create your views here.
from .models import *


def home(request):
    jobs = Jobs.objects.all()
    context = {'jobs':jobs}
    return render(request, 'core/home.html', context)


def operation(request):
    return render(request, 'core/operation.html')

def signin(request):
    return render(request, 'core/signin.html')

def signup(request):
    return render(request, 'core/signup.html')

def workers(request):
    return render(request, 'core/workers.html')

def myclients(request):
    clients = Clients.objects.all()
    context = {'clients':clients}
    return render(request, 'core/clients.html', context)

def clientdetails(request, name):
    clients = get_object_or_404(Clients, name=name)
    measurement = get_object_or_404(ClientMeasurements, name=name)
    context = {'clients':clients,
               'measurement': measurement,
               }
    return render(request, 'core/clientdetails.html', context)

def job_done(request):
    jobdones =Job_operation.objects.all()
    context = {'jobdones':jobdones}
    return render(request, 'core/home.html', context)