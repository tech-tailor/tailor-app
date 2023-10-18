from twilio.rest import Client
from django.conf import settings
 
 
 
def send_verification_code(phone_number, verification_code):
        account_sid = settings.TWILIO_ACCOUNT_SID
        auth_token = settings.TWILIO_AUTH_TOKEN
        twilio_phone_number = settings.TWILIO_PHONE_NUMBER
        
        try:
            
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                to=phone_number,
                messaging_service_sid='MG930c177f6809ab1ae72f2e98e27329a4',
                body=f"Your verification code: {verification_code}"
            )
            print('verification succesful')
            return verification_code
        
        except Exception as e:
            # Handle exceptions (e.g., invalid phone number, Twilio errors)
            print(f"Error sending verification code: {e}")
            return None
