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
    webhook =  os.getenv('WEBHOOK_URL')
    headers = {
                "Content-Type":"application/json",
              }
    msg_json = json.dumps( { "content":msg } )

    r = requests.post(webhook, headers=headers, data=msg_json)
    print (r)
