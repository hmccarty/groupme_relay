import os
import json
import requests

from urllib.parse import urlencode
from urllib.request import Request, urlopen

from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()

    if data['name'] != 'Groupme-Relay':
       msg = '{}, you sent "{}".'.format(data['name'], data['text'])
       send_message(msg)

    return "ok", 200

def send_message(msg):
    url = "https://discordapp.com/api/channels/{}/messages".format(channel)
    headers= {
                "Authorization":"Bot {}".format(os.getenv('DISCORD_TOKEN')),
                "User-Agent":"GroupMeRelay",
                "Content-Type":"application/json",
             }
    channel =  os.getenv('DISCORD_CHANNEL')
    msg_json = json.dumps( { "content":msg } )

    r = requests.post(url, headers=headers, data=msg_json)
