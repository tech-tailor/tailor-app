from django import forms






class PhoneNumberForm(forms.Form):
    phone_number = forms.CharField(
        label='Phone number',
        widget=forms.TextInput(attrs={'placeholder': '+234XXXXXXXXXXX'}),
        max_length=15,
        required=True,
    )
    
 
    
    
class VerifyCode(forms.Form):
    verify_code = forms.CharField(
        label='verify code',
        widget=forms.TextInput(attrs={'placeholder': 'enter code'}),
        max_length=15,
        required=True,
    )
    

