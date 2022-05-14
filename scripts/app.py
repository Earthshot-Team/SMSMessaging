from flask import Flask, request
from twilio import twiml

app = Flask(__name__)


@app.route('/sms', methods=['POST'])
def sms():
    # print request.form to see all the other options
    number = request.form['From']
    message_body = request.form['Body']

    resp = twiml.Response()
    resp.message(f'Hello {number}, you said: {message_body}')
    return str(resp)

if __name__ == '__main__':
    app.run()