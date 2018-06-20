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
sys.path.append('/home/pi/xiaolan/')
from speech_center.conversation import dialogue
from display_center.display import screen
import setting

class skills(object):

    def __init__(self):
        pass
    def skillReq(self, url, intent, slots, intentdict):

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
    
    def skillTryLive(self, url):
        
        data = {
            'ClientEvent': {
                'Header': {
                    'Type': 'TestSkillAlive'
                    'FromPlatfrom': 'from_user',
                    'ShouldHandlerType': 'TestSkillAlive'
                },
                'ConversationLog': {
                    'Type': None
                }
            },
            'ClientLog': {
                'ClientType': setting.setting()['main_setting']['device_type'],
                'RequestsID': None,
                'Key': 'xiaolanserverpasswordYYH',
            }
            'SpecialNeed': None
        }
        r = requests.post(url,
                          data=json.dumps(data))
        json = r.json()
        return json['state']
        
    def command(self, json):

        s = screen()
        d = dialogue()
        m = music()
        commands = json['commands'][0]
        if commands == 'Ask':
            respones = d.ask(json['commands'][1]['text'], json['commands'][1]['slot'], json['commands'][1]['recordtype'])
            r = requests.post(url,
                              data=json.dumps({'states': 'ASKturnback', 'key': 'xiaolanserverpasswordYYH', 'askturn': respones}))
        elif commands == 'MusicPlay':
            musicurl = json['commands'][1]
            m.download(musicurl)
            speaker.play(json['commands'][2])
        elif commands == 'MusicStop':
            speaker.stop()
        elif comamnds == '
        
