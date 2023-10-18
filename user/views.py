from django.shortcuts import render, redirect
from django.conf import settings
from twilio.rest import Client
from user.forms import PhoneNumberForm, VerifyCode
from django import forms
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from user.twillo import send_verification_code
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from .models import CustomUser
from django.contrib import messages


def phonenumber(request):
    if request.method == "POST":
        form = PhoneNumberForm(request.POST)
        if form.is_valid():
            # Get the user-submitted code
            phone_number = form.cleaned_data['phone_number']
            print(phone_number)
            verification_code = 6666
            
            user=request.user
            user.phone_number=phone_number
            user.verify_code=verification_code
            user.save()
            send_verification_code(phone_number, verification_code)
            return redirect('verifycode')
        
    else:    
        form = PhoneNumberForm()
    return render(request, 'user/phonenumberform.html', {'form': form})

def verify_code(request):
    if request.method == "POST":
        form = VerifyCode(request.POST)
        if form.is_valid():
            # Get the user-submitted code
            verify_code = form.cleaned_data['verify_code']
            print(verify_code)
            
            user = request.user
            if user.verify_code == verify_code:
                user.verified = True
                user.save()
                messages.success(request, 'Phone number verification was successful.')
                
                return redirect('verifycode')

            else:
                messages.success(request, 'Invalid verification code')
                return redirect('verifycode')
    else:
        form = VerifyCode()
    return render(request, 'user/verify_code.html', {'form': form})