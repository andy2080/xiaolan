# -*- coding: utf-8 -*-

import sys
import os
import time
import requests
import json
sys.path.append('/home/pi/xiaolan/')
import setting

def intentlistturn():
    url = ''
    data = {
            'ClientEvent': {
                'Header': {
                    'NameSpace': 'xiaolan.client.intentlist.get',
                    'TimeStamp': int(time.time()),
                    'RequestsId': time.time(),
                    'RequestsFrom': setting.setting()['main_setting']['clienttype'],
                    'ClientId': setting.setting()['main_setting']['clientid']
                },
                'ConversationInfo': {
                    'ConversationId': None,
                    'ShouldHandlerSkill': None,
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
                    'NluStates': ['waitIntentList'],
                    'SttStates': ['emptying'],
                    'TtsStates': ['emptyling']
                },
                'Commands': {
                    'ClientCommands': ['service for user'],
                    'elseCommands': []
                }
            }
        }
    r = requests.post(url,
                      data=data)
    return r.json()
