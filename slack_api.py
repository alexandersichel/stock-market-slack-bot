# https://slack.com/api/rtm.start

import os, requests, websocket, json
# print (os.environ)
from idgenerator import id_generator
from market_bot import generate_output

bot_token = os.environ['HackerBotToken']
print (bot_token)

def get_websocket_url():
    response = requests.get ('https://slack.com/api/rtm.start', params = {'token' : bot_token})
    if response.ok and ('url' in response.json()):
        return (response.json()['url'])
    else:
        print ('Error Getting url:')
        print (response.text)

def connect(websocket_url):
    ws = websocket.WebSocketApp (websocket_url,
                                on_message = on_message,
                                on_error = on_error)
    ws.run_forever()

def on_message(ws, data):
    print ('Data Received!!')
    data = json.loads(data)
    if 'type' in data and data['type']== 'message':
        # if message has "hello," say "hello" back.
        print (data)
        input_message = data['text']
        if '<@U4NEMV8DS>' in input_message:
            channel = data['channel']
            unique_id = id_generator.get_unique_id()
            print('unique_id', unique_id)
            reply = {
                "id": unique_id,
                "type": "message",
                "channel": channel,
                "text": generate_output(input_message)
                }
            ws.send(json.dumps(reply))

def on_close(ws):
    print ('Websocket Closing')
def on_error (ws, error):
    print ('Error')
    print (error)


