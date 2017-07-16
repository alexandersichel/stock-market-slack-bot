from slack_api import *
from flask import Flask
import os

app = Flask (__name__)

# @ = decorator setting up an API end point of the method below it
@app.route ('/', methods = ['GET'])
def main_page():
    return 'hello world'

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