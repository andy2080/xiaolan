# -*- coding: utf-8 -*-

import sys
import os
import json
import demjson
import requests
import hashlib
import base64
import time
from xiaolanServerCommandDo import CommandsDo
sys.path.append('/home/pi/xiaolan/')
import setting

class ClientToServer(object):

    def __init__(self):

        self.url = setting.setting()['main_setting']['url']
    
    def ClientDiyReq(self, data):
        
        r = requests.post(self.url,
                          data=data)
        return r.json()
    
    def DiyReq(self, data):
        
        r = requests.post(self.url,
                          data=data)
        return r.json()
    
    def ClientSkillAskSlotsRes(self, slots, text):
        
        data = {
            'ClientEvent': {
                'Header': {
                    'NameSpace': None,
                    'TimeStamp': int(time.time()),
                    'RequestsId': '7636',
                    'RequestsFrom': setting.setting()['main_setting']['ClientType'],
                    'ClientId': setting.setting()['main_setting']['ClientId']
                },
                'ConversationInfo': {
                    'ConversationId': None,
                    'ShouldHandlerSkill': None,
                    'SkillShouldHandler': None,
                    'SkillAwakenKeyword': None,
                    'SendToSkillInfo': {
                        'Intent': None,
                        'Text': text,
                        'Slots': slots
                    }
                }
            },
            'Debug': {
                'TimeStamp': str(int(time.time())),
                'ClientId': setting.setting()['main_setting']['clientid'],
                'States': {
                    'ClientStates': ['serviceing'],
                    'NluStates': ['working'],
                    'SttStates': ['emptying'],
                    'TtsStates': ['emptying']
                },
                'Commands': {
                    'ClientCommands': ['service for user'],
                    'elseCommands': []
                }
            }
        }
    
    def ClientReq(self, intent, slots, intentdict):

        sk = skills()
        data = {
            'ClientEvent': {
                'Header': {
                    'NameSpace': intent,
                    'TimeStamp': int(time.time()),
                    'RequestsId': time.time(),
                    'RequestsFrom': setting.setting()['main_setting']['ClientType'],
                    'ClientId': setting.setting()['main_setting']['ClientId']
                },
                'ConversationInfo': {
                    'ConversationId': '456564889456',
                    'ShouldHandlerSkill': intentdict['skill'],
                    'SkillShouldHandler': intent,
                    'SkillAwakenKeyword': intentdict['keyword'],
                    'SendToSkillInfo': {
                        'Intent': intent,
                        'Text': intentdict['text'],
                        'Slots': slots
                    }
                }
            },
            'Debug': {
                'TimeStamp': str(int(time.time())),
                'ClientId': setting.setting()['main_setting']['clientid'],
                'States': {
                    'ClientStates': ['serviceing'],
                    'NluStates': ['working'],
                    'SttStates': ['working'],
                    'TtsStates': ['emptying']
                },
                'Commands': {
                    'ClientCommands': ['service for user'],
                    'elseCommands': []
                }
            }
        }
        r = requests.post(self.url,
                          data=json.dumps(data))
        sk.command(r.json())
    
    def ClientTrySkillLive(self, skillname):
        
        data = {
            'ClientEvent': {
                'Header': {
                    'NameSpace': 'xiaolan.client.skill.tryalive',
                    'ServerShouldHandler': 'tryskillalive',
                    'TimeStamp': int(time.time()),
                    'RequestsId': time.time(),
                    'RequestsFrom': setting.setting()['main_setting']['clienttype'],
                    'ClientId': setting.setting()['main_setting']['clientid']
                },
                'ConversationInfo': {
                    'ConversationId': None,
                    'ShouldHandlerSkill': skillname,
                    'SkillShouldHandler': None,
                    'SkillAwakenKeyword': None,
                    'SendToSkillInfo': {
                        'Intent': None,
                        'Text': None,
                        'Slots': None
                    }
                }
            },
            'Debug': {
                'TimeStamp': str(int(time.time())),
                'ClientId': setting.setting()['main_setting']['clientid'],
                'States': {
                    'ClientStates': ['serviceing'],
                    'NluStates': ['emptyling'],
                    'SttStates': ['emptying'],
                    'TtsStates': ['emptying']
                },
                'Commands': {
                    'ClientCommands': ['service for user'],
                    'elseCommands': []
                }
            }
        }
        r = requests.post(self.url,
                          data=json.dumps(data))
        json = r.json()
        return json['state']
