import os
import json
import discord

from urllib.parse import urlencode
from urllib.request import Request, urlopen

from flask import Flask, request

app = Flask(__name__)
client = discord.Client()

@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()

    if data['name'] != 'Groupme-Relay':
       msg = '{}, you sent "{}".'.format(data['name'], data['text'])
       send_message(msg)

    return "ok", 200

def send_message(msg):
    channels =  os.getenv('DISCORD_CHANNELS').split(' ')

    for guild in guilds:
        for channel in guild.channels:
            if channel.name in channels:
                channel.send(msg)
    """
    data = {
        'bot_id' : os.getenv('GROUPME_BOT_ID'),
        'text'   : msg,
    }

    request = Request(url, urlencode(data).encode())
    json = urlopen(request).read().decode()
    """

client.run(os.getenv('DISCORD_TOKEN'))
