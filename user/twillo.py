from twilio.rest import Client
from decouple import config
import logging
 
 
def send_verification_code(phone_number, verification_code):
    # Get an instance of the logger for your app
    logger = logging.getLogger(__name__)
        
    try:
        account_sid = config('TWILIO_ACCOUNT_SID')
        auth_token = config('TWILIO_AUTH_TOKEN')
        twilio_phone_number = config('TWILIO_PHONE_NUMBER')
        
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            to=phone_number,
            messaging_service_sid=config('messaging_service_sid'),
            body=f"Your verification code: {verification_code}"
        )
        print('verification succesful')
        return verification_code
    
    except Exception as e:
        # Handle exceptions (e.g., invalid phone number, Twilio errors)
        logger.error(f"Error sending verification code: {e}")
        return None
