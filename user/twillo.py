from twilio.rest import Client
from decouple import config
 
 
 
def send_verification_code(phone_number, verification_code):
        account_sid = config(TWILIO_ACCOUNT_SID)
        auth_token = config(TWILIO_AUTH_TOKEN)
        twilio_phone_number = config(TWILIO_PHONE_NUMBER)
        
        try:
            
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                to=phone_number,
                messaging_service_sid=config(messaging_service_sid),
                body=f"Your verification code: {verification_code}"
            )
            print('verification succesful')
            return verification_code
        
        except Exception as e:
            # Handle exceptions (e.g., invalid phone number, Twilio errors)
            print(f"Error sending verification code: {e}")
            return None
