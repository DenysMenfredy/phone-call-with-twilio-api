import os
from dotenv import load_dotenv
from twilio.rest import Client
import argparse


def main():
    load_dotenv() # load environment variables from .env file

    account_sid = os.getenv('TWILIO_ACCOUNT_SID') 
    auth_token = os.getenv('TWILIO_AUTH_TOKEN')
    my_number = str(os.getenv('MY_NUMBER'))
    ap = argparse.ArgumentParser()
    ap.add_argument("--to", "--numbertocall", required=True, 
                    help="number to call")
    
    args = vars(ap.parse_args())
    number_to_call = args['to']

    client = Client(account_sid, auth_token)


    response_url = 'http://demo.twilio.com/docs/voice.xml' #example of a call from twilio api

    call = client.calls.create(
        url=response_url,
        to=f'+55{number_to_call}', 
        from_=my_number 
    )

    print(call.sid)


if __name__ == '__main__':
    main()