from slack_api import *

url = get_websocket_url()
connect (url)

# ws.send("Hello %d" % i)
#
# {
#     "id": 1,
#     "type": "message",
#     "channel": "C024BE91L",
#     "text": "Hello world"
# }