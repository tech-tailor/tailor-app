import phonenumbers
from phonenumbers.phonenumberutil import NumberParseException
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.conf import settings
from user.forms import PhoneNumberForm, VerifyCode
from django.urls import reverse
from django.contrib.auth import get_user_model
from user.twillo import send_verification_code
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from store.models import TemporaryPhoneNumber


def phone_number_verification(request, phone_number):
    try:
        if  request.user.is_authenticated:
            try:
                parsed_number = phonenumbers.parse(phone_number, None)
                if not phonenumbers.is_valid_number(parsed_number):
                    messages.error(request, "Invalid phone number")
                    #return redirect('verifyphone')
            except NumberParseException  as e:
                messages.error(request, e)
                #return redirect('verifyphone')
            
            # Check if the phone number is already associated with a user
            User = get_user_model()
            try:
                if User.objects.get(phone_number=phone_number):
                    messages.error(request, "This phone number is already in use.")
                    #return redirect('verifyphone')
            except ObjectDoesNotExist:
                pass
            
            verification_code = 6666
            
            
            temp_phone=TemporaryPhoneNumber(user=request.user)
            temp_phone.phone_number = phone_number
            temp_phone.verification_code = verification_code
            temp_phone.save()
            send_verification_code(phone_number, verification_code)
            #return redirect('verifycode')
        
        else:
            messages.error(request, 'You are not logged in')
            messages.error(request, 'You will be redirected to the login page in 5sec')
            return redirect('account_login')
            
    except ValueError:
        messages.error(request, 'You are not logged in')
        messages.error(request, 'You will be redirected to the login page in 5sec')
        #time.sleep(10)
        return redirect('account_login')
    
    
def phone_code_verification(request, phone_number):
    try:
        temp_code = TemporaryPhoneNumber.objects.get( user=request.user)
        if temp_code.verification_code == verify_code:
            user = request.user
            user.phone_number = temp_code.phone_number
            user.verified = True
            user.save()
            
            TemporaryPhoneNumber.objects.get(verification_code=verify_code, user=request.user).delete()
            messages.success(request, 'Phone number verification was successful.')
            url = reverse('store_clientdetails', args=[request.user.phone_number])
            return redirect(url)
            
        else:
            TemporaryPhoneNumber.objects.filter(verification_code=verify_code, user=request.user).delete()
            messages.error(request, 'Invalid verification code')
            return redirect('verifycode')

    except TemporaryPhoneNumber.MultipleObjectsReturned:
        temp_code = TemporaryPhoneNumber.objects.filter(user=request.user)
        temp_code.delete()
        messages.error(request, 'Invalid verification code, code requested several times')
        messages.error(request, 'Try Again!')
        return redirect('verifycode')
    except TemporaryPhoneNumber.DoesNotExist :
        temp_code = TemporaryPhoneNumber.objects.filter(user=request.user)
        temp_code.delete()
        messages.error(request, 'Invalid verification code, no code has been requested for')
        messages.error(request, 'Try Again!')
        return redirect('verifycode')