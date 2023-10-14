from django.urls import register_converter
from phonenumbers import parse 

class PhoneNumberConverter:
    regex = r'\+?[0-9]+'
    
    def to_python(self, value):
        return parse(value)
    
    def to_url(self, value):
        return str(value)
    
register_converter(PhoneNumberConverter, 'phone')
