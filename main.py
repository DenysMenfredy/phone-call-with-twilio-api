import os
from dotenv import load_dotenv
from twilio.rest import Client


load_dotenv()

account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')

client = Client(account_sid, auth_token)

response_url = 'https://handler.twilio.com/twiml/EHa29a0f5d1b5526a0e2fad5d46dec31b0'

call = client.calls.create(
    url=response_url,
    to='+5591993213967',
    from_='+12312599889'
)

print(call.sid)