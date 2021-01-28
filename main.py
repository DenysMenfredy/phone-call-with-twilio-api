import os
from dotenv import load_dotenv
from twilio.rest import Client


load_dotenv()

account_sid = os.getenv('TWILIO_ACCOUNT_SID') # put your twilio account_sid here
auth_token = os.getenv('TWILIO_AUTH_TOKEN') # put your twilio auth_token here

client = Client(account_sid, auth_token)

response_url = 'https://handler.twilio.com/twiml/EHa29a0f5d1b5526a0e2fad5d46dec31b0'

call = client.calls.create(
    url=response_url,
    to='', # put your number registered in twilio here
    from_='' # put the number you wanna call here
)

print(call.sid)