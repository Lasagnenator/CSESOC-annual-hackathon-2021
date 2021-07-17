from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    """Respond to incoming messages with a simple text message."""
    
    resp = MessagingResponse()
    resp.message("Your message has been received.")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
