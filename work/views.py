import time
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from tailorApp.util import phone_code_verification, phone_number_verification
from  work.decorators import verify_worker_required
from work.forms import WorkerForm
from django.contrib import messages

# Create your views here.
from .models import *

@login_required
@verify_worker_required
def jobs(request):
    try:
        jobs = Jobs.objects.all().order_by('-id')
        jobdones =Job_operation.objects.all()
        context = {'jobs':jobs,
                'jobdones':jobdones,
                }
        return render(request, 'work/jobs.html', context)
    except Exception as e:
        print('error: {e}')
        return redirect('work_worker_form')
        

@login_required
@verify_worker_required
def operation(request):
    return render(request, 'work/operation.html')




@login_required
def myprofile(request):
    try:
        worker = Worker_Profile.objects.get(user=request.user)
        context = {
            'worker': worker
        }
        return render(request, 'work/profile.html', context)
    except Exception as e:
        print('error: {e}')
        return redirect('work_worker_form')
        
        
@login_required
def home(request):
    context = {}
    return render(request, 'work/home.html', context)

@staff_member_required
@login_required
def client(request):
    clients = Clients.objects.all().order_by('measurement_name', '-id')
    context = {'clients':clients}
    return render(request, 'work/client.html', context)

@login_required
@verify_worker_required
def clientdetails(request, measurement_name):
    clients = get_object_or_404(Clients, measurement_name=measurement_name)
    context = {'clients':clients}
    return render(request, 'work/clientdetails.html', context)

@login_required
@verify_worker_required
def clientmeasurement(request, measurement_name):
    clients = Clients.objects.get(measurement_name=measurement_name)
    context = {'clients':clients}
    return render(request, 'work/measurement.html', context)
    
@login_required
@verify_worker_required
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

@staff_member_required
@login_required
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


@login_required
def worker_form(request):
    if request.method == "POST":
        form = WorkerForm(request.POST)
        if form.is_valid():
            #phone_number = form.cleaned_data['Phone_Number']
            firstname = form.cleaned_data['first_name']
            lastname = form.cleaned_data['last_name']
            sex = form.cleaned_data['sex']
            print(lastname)
            
            try:
                if request.user.is_authenticated:
                    #phone_number_verification(request, phone_number)
                    #phone_code_verification(request, phone_number)
                    Worker_Profile.objects.update_or_create(
                        user=request.user,
                        defaults={
                            'sex': sex,  
                        }
                    )
                    user = request.user
                    user.first_name = firstname
                    user.last_name= lastname
                    #user.phone_number = phone_number,
                    #user.verified = True
                    user.save()
                    #messages.success(request, 'Phone number verification was successful.')
                    print('success')
                    return redirect('work_home')
                else:
                    pass
            except Exception as e:
                print(f'error: {e}')
    else:
        pass
        form = WorkerForm()
    return render(request, 'work/worker_form.html', {'form': form})  