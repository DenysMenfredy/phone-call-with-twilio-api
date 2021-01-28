from flask import Flask
from twilio.twiml.voice_response import Play, VoiceResponse


app = Flask(__name__)
    
@app.route("/")
def home():
    return 'server running'
     
@app.route("/call", methods=['POST'])
def call():
    response = VoiceResponse()
    response.play('https://api.twilio.com/cowbell.mp3', loop=10)
        
    return str(response)

    
if __name__ == "__main__":
    app.run(host='0.0.0.0')