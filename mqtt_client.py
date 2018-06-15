import random
import sys, os
import subprocess
import time
import urllib2

from Adafruit_IO import MQTTClient

from mpd import (MPDClient, CommandError)


with open('config.json', 'r') as f:
    conf = json.load(f)

ADAFRUIT_IO_KEY      = conf["ADAFRUIT_IO_KEY"]
ADAFRUIT_IO_USERNAME = conf["ADAFRUIT_IO_USERNAME"]                                    
ADAFRUIT_FEED        = conf["ADAFRUIT_FEED"]
enigma2_url = conf["enigma2_url"]

pathname = os.path.dirname(sys.argv[0])
path = os.path.abspath(pathname) + '/'


def get_command(text):
    return text.split()[0]

def get_params(text):
    return text.replace(get_command(text)+' ', '')

def connected(client):
    print('Connected to Adafruit IO!  Listening for foto feed changes...')
    client.subscribe(ADAFRUIT_FEED)

def disconnected(client):
    print('Disconnected from Adafruit IO!')
    sys.exit(1)

def message(client, feed_id, payload, retain):
    command = get_command(payload)
    params = get_params(payload)

    if command == "show":
        print('Feed {0} received new value: {1}'.format(feed_id, payload))
        params = payload.replace("show ", " ")
        cmd = path + 'slideshow.sh {1}'.format(feed_id, params)
        subprocess.Popen(cmd, shell=True).wait()
    if command == "tv":
        host = "http://192.168.1.180/"
	url = enigma2_url
	if params == "turn on":
           url += "api/powerstate?newstate=0"
	if params == "turn off":
           url += "api/powerstate?newstate=0"
	    print url
        content = urllib2.urlopen(url).read()
	    print content
    if command == "music":
        HOST = "192.168.1.195"
        PORT = 6600
        client = MPDClient()
        client.connect(host=HOST, port=PORT)
	if params == "play":
            client.play()
        if params == "stop":
            client.stop()
        if params == "pause":
            client.pause()
        if params == "next":
            client.next()
        client.disconnect()

client = MQTTClient(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

client.on_connect    = connected
client.on_disconnect = disconnected
client.on_message    = message

client.connect()
client.loop_blocking()
