from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
from twilio.twiml.voice_response import VoiceResponse
from database import QuestionQueue, HTML_queue

Qqueue = QuestionQueue("database.json")

app = Flask(__name__)

@app.route("/sms", methods=['GET'])
def sms_reply():
    """Save the sms message and send a confirmation message back."""
    body = request.values.get('Body', None)
    app.logger.debug("sms received: {}".format(body))
    Qqueue.enqueue(body)
    Qqueue.save()
    
    resp = MessagingResponse()
    resp.message("Your message has been received.")

    return str(resp)

@app.route("/call", methods=['GET', 'POST'])
def call():
    """Record The incoming call."""
    response = VoiceResponse()
    response.say('Hello. Please leave your question after the beep.')
    response.record()
    response.hangup()

    # Message is not saved here but on Twilio console.
    # Add a link to it in the queue
    Qqueue.enqueue("RECORDED CALL --- https://www.twilio.com/console/voice/recordings/recording-logs/")
    Qqueue.save()

    return str(response)

@app.route("/", methods=['GET'])
@app.route("/queue", methods=['GET'])
def queue():
    "Give the question queue."
    return HTML_queue(Qqueue)

if __name__ == "__main__":
    app.run(debug=True)
