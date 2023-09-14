from django.shortcuts import get_object_or_404, render

# Create your views here.
from .models import *


def home(request):
    jobs = Jobs.objects.all().order_by('-id')
    jobdones =Job_operation.objects.all()
    context = {'jobs':jobs,
               'jobdones':jobdones,
               }
    return render(request, 'core/home.html', context)


def operation(request):
    return render(request, 'core/operation.html')


def signin(request):
    return render(request, 'core/signin.html')

def signup(request):
    return render(request, 'core/signup.html')

def myprofile(request):
    profile = Workers.objects.filter(name=User)
    context = {'profile':profile}
    return render(request, 'core/profile.html', context)

def client(request):
    clients = Clients.objects.all().order_by('name', '-id')
    context = {'clients':clients}
    return render(request, 'core/client.html', context)

def clientdetails(request, name, measurement_id):
    measurement = get_object_or_404(ClientMeasurements, name=name)
    clients = get_object_or_404(Clients, measurement_id=measurement_id)
    context = {'clients':clients,
               'measurement': measurement,
               }
    return render(request, 'core/clientdetails.html', context)

def jobdetails(request, id):
    jobs = Jobs.objects.get(id=id)
    fabric_image_1_url = jobs.image_url('fabric_image_1')
    fabric_image_2_url = jobs.image_url('fabric_image_2')
    top_design_image_1_url = jobs.image_url('top_design_image_1')
    top_design_image_2_url = jobs.image_url('top_design_image_2')
    trouser_design_image_url = jobs.image_url('trouser_design_image')
    agbada_design_image_url = jobs.image_url('agbada_design_image')
    cap_fabric_image_url = jobs.image_url('cap_fabric_image')
    cap_design_image_url = jobs.image_url('cap_design_image')
    context = {
        'jobs':jobs,
        'fabric_image_1_url':fabric_image_1_url,
        'fabric_image_2_url':fabric_image_2_url,
        'top_design_image_1_url':top_design_image_1_url,
        'top_design_image_2_url':top_design_image_2_url,
        'trouser_design_image_url':trouser_design_image_url,
        'agbada_design_image_url':agbada_design_image_url,
        'cap_fabric_image_url':cap_fabric_image_url,
        'cap_design_image_url':cap_design_image_url,
        }
    return render(request, 'core/jobdetails.html', context)