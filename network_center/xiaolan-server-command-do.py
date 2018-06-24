# -*- coding: utf-8 -*-

import sys
import os
import json
import base64
import hashlib
import requests
import time
import xiaolanClientToServer
sys.path.append('/home/pi/xiaolan/')
from memory_center.commandlist import clist
from speech_center.conversation import dialogue

class CommandsDo(object):
  
    def _init__(self):
        self.xcts = xClientToServer()
    def Do(self, respones):
        syscommands = respones['ClientShouldDo']['System']['commands']
        sysmore = respones['ClientShouldDo']['System']['more']
        if syscommands == 'ShutDown':
            os.system('sudo poweroff')
        elif syscommands == 'Reboot':
            os.system('sudo reboot')
        elif syscommands == 'SendLog':
            data = {
                        'ClientEvent': {
                            'Header': {
                                'NameSpace': 'ClientLog',
                                'TimeStamp': int(time.time),
                                'RequestsId': '8476',
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
                                      'Text': None,
                                      'Slots': {
                                          'slot1': None
                                      }
                                }
                            }
                        },
                        'Debug': {
                            'TimeStamp': str(time.time()),
                            'ClientId': setting.setting()['main_setting']['ClientId'],
                            'States': {
                                'ClientStates': ['working'],
                                'NluStates': ['emptying'],
                                'SttStates': ['emptying'],
                                'TtsStates': ['emptying']
                            },
                            'Commands': {
                                'ClientCommands': [],
                                'elseCommands': []
                            }
                        }
            }
            self.xcts.DiyReq(data)
        elif syscommands == '
        
