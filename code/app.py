import os

from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse, Message

from mars import get_mars_photo_url


app = Flask(__name__)


@app.route('/sms', methods=['POST'])
def inbound_sms():
    message_body = request.form['Body']
    resp = MessagingResponse()

    if message_body.isdigit():
        response_message = 'Taken {0} Martian solar days into the journey.' \
                           .format(message_body)
        photo_url = get_mars_photo_url(message_body)

        msg = Message().body(response_message).media(photo_url)
        resp.append(msg)
    else:
        msg = Message().body('Text a number of solar days into the rover\'s journey.')
        resp.append(msg)

    return str(resp)


if __name__ == '__main__':
    app.run()
