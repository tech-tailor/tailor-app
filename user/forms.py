from django import forms
from django.shortcuts import render, redirect
from django.urls import reverse
import phonenumbers
from phonenumbers.phonenumberutil import NumberParseException
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist

from user.twillo import send_verification_code



class PhoneNumberForm(forms.Form):
    phone_number = forms.CharField(
        label='Phone number',
        widget=forms.TextInput(attrs={'placeholder': '+234XXXXXXXXXXX'}),
        max_length=15,
        required=True,
    )
    
 
    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        try:
            parsed_number = phonenumbers.parse(phone_number, None)
            if not phonenumbers.is_valid_number(parsed_number):
                raise forms.ValidationError("Invalid phone number")
        except NumberParseException  as e:
            raise forms.ValidationError(e)
    
      # Check if the phone number is already associated with a user
        User = get_user_model()
        try:
            if User.objects.get(phone_number=phone_number):
                raise forms.ValidationError("This phone number is already in use.")
        except ObjectDoesNotExist:
            pass
        
        
        
        
        return phone_number
    
class VerifyCode(forms.Form):
    verify_code = forms.CharField(
        label='verify code',
        widget=forms.TextInput(attrs={'placeholder': 'enter code'}),
        max_length=15,
        required=True,
    )
    
    def clean_phone_number(self):
        verify_code = self.cleaned_data.get('verify_code')
        try:
            parsed_number = len(verify_code)
            print(parsed_number)
            if parsed_number != 4:
                raise forms.ValidationError("Invalid code")
        except ValueError  as e:
            raise forms.ValidationError(e)

