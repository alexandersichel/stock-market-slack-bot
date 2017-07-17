from slack_api import *
from flask import Flask, request
import os
from slacker import Slacker


app = Flask (__name__)
Slack_bot = Slacker(os.environ['HackerBotToken'])

# @ = decorator setting up an API end point of the method below it
@app.route ('/', methods = ['GET'])
def main_page():
    return 'hello world'

@app.route ('/', methods = ['POST'])
def received_webhook ():
    data = request.form
    print ('Receiving Webhook Data')
    print (data)
    channel_id = data.get('channel_id')
    text = data.get ('text')
    response = generate_output ('text')
    Slack_bot.chat.post_message(channel_id, response)
    return 'Data Sent'


app.run (host = '0.0.0.0', port = os.environ.get("PORT",8080))

# url = get_websocket_url()
# connect (url)

# ws.send("Hello %d" % i)
#
# {
#     "id": 1,
#     "type": "message",
#     "channel": "C024BE91L",
#     "text": "Hello world"
# }