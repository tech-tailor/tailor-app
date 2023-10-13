import time
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


# Create your views here.
from .models import *


def home(request):
    jobs = Jobs.objects.all().order_by('-id')
    jobdones =Job_operation.objects.all()
    context = {'jobs':jobs,
               'jobdones':jobdones,
               }
    return render(request, 'work/home.html', context)


def operation(request):
    return render(request, 'work/operation.html')




@login_required
def myprofile(request):
    context = {}
    return render(request, 'work/profile.html', context)

def client(request):
    clients = Clients.objects.all().order_by('measurement_name', '-id')
    context = {'clients':clients}
    return render(request, 'work/client.html', context)

def clientdetails(request, measurement_name):
    clients = get_object_or_404(Clients, measurement_name=measurement_name)
    context = {'clients':clients}
    return render(request, 'work/clientdetails.html', context)

def clientmeasurement(request, measurement_name):
    clients = Clients.objects.get(measurement_name=measurement_name)
    context = {'clients':clients}
    return render(request, 'work/measurement.html', context)
    

def jobdetails(request, job_name):
    jobs = Jobs.objects.get(job_name=job_name)
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
    return render(request, 'work/jobdetails.html', context)


def error_log(request):
    try:
        with open('error.test', 'r') as log_file:
            log_content = log_file.read()

            if len(log_content) == 0:
                log_content = "No error yet, file is empty"
            
        with open('error.test', 'w') as log_file:
            log_file.write("file deleted after refresh\n")

    except FileNotFoundError:
        log_content = "Error log not found"

    return HttpResponse(log_content, content_type='text/html', status=200)
