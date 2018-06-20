# -*- coding: utf-8 -*-

import sys
import os
import json
import demjson
import requests
import httplib
import urllib
import urllib2
import hashlib
import base64
from music import music
sys.path.append('/home/pi/xiaolan/')
from speech_center.conversation import dialogue
from display_center.display import screen

class skills(object):

    def __init__(self):
        pass
    def req(self, url, intent, slots, intentdict):

        sk = skills()
        data = {
            'intent': intent,
            'slots': slots,
            'intentdict': intentdict,
            'key': 'xiaolanserverpasswordYYH'
            'states': 'NEWconversation'
            }
        r = requests.post(url,
                          data=json.dumps(data))
        sk.command(r.json())

    def command(self, json):

        s = screen()
        d = dialogue()
        m = music()
        commands = json['commands'][0]
        if commands == 'ask':
            respones = d.ask(json['commands'][1]['text'], json['commands'][1]['slot'], json['commands'][1]['recordtype'])
            r = requests.post(url,
                              data=json.dumps({'states': 'ASKturnback', 'key': 'xiaolanserverpasswordYYH', 'askturn': respones}))
        elif commands == 'MusicPlay':
            musicurl = json['commands'][1]
            m.download(musicurl)
            speaker.play(json['commands'][2])
        elif commands == 'MusicStop':
            speaker.stop()
        
