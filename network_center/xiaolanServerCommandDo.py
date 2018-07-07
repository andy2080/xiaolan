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
import setting
# from memory_center.log import Log
# from memory_center.commandlist import clist
from speech_center.conversation import dialogue

class CommandsDo(object):
  
    def _init__(self):
        self.xcts = xClientToServer()
        self.l = Log()
        self.d = dialogue()
    def Do(self, respones):
        syscommands = respones['ClientShouldDo']['System']['commands']
        # SystemCommands
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
                            },
                            'ClientLog': sel.l.GetLog()
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
        # ScreeDisplay
        Type = respones['ClientShouldDo']['Skill']['ScreeDisplay']['Type']
        if Type == 'TextDisplay':
            Title = respones['ClientShouldDo']['Skill']['ScreeDisplay']['Title']
            Text = respones['ClientShouldDo']['Skill']['ScreeDisplay']['Text']
            Remind = respones['ClientShouldDo']['Skill']['ScreeDisplay']['RemindWord']
        elif Type == 'ImageDisplay':
            Title = respones['ClientShouldDo']['Skill']['ScreeDisplay']['Title']
            ImageUrl = respones['ClientShouldDo']['Skill']['ScreeDisplay']['ImageUrl']
            RemindWord = respones['ClientShouldDo']['Skill']['ScreeDisplay']['RemindWord']
        elif Type == 'VideoDisplay':
            Title = respones['ClientShouldDo']['Skill']['ScreeDisplay']['Title']
            VideoUrl = respones['ClientShouldDo']['Skill']['ScreeDisplay']['VideoUrl']
            RemindWord = respones['ClientShouldDo']['Skill']['ScreeDisplay']['RemindWord']
        elif Type == 'MusicDisplay':
            Title = respones['ClientShouldDo']['Skill']['ScreeDisplay']['Title']
        # OutputSpeech
        if respones['ClientShouldDo']['Skill']['OutputSpeech'] != None or respones['ClientShouldDo']['Skill']['OutputSpeech'] != '':
            self.d.tts_text(respones['ClientShouldDo']['Skill']['OutputSpeech'], respones['ClientShouldDo']['Skill']['TtsService'], respones['ClientShouldDo']['Skill']['TtsMore'])
        else:
            pass
        # AskSlots
        if respones['ClientShouldDo']['Skill']['AskSlots'] != None or respones['ClientShouldDo']['Skill']['AskSlots'] != '':
            slotsturn = self.f.AskSlots(respones['ClientShouldDo']['Skill']['AskSlots']['SlotsName'], respones['ClientShouldDo']['Skill']['AskSlots']['SlotDict'], respones['ClientShouldDo']['Skill']['AskSlots']['RecordType'])
            self.xcts.SkillAskSlotsRes(slotsturn['slots'], slotsturn['text'])
        else:
            pass
        # WaitAnswer
        if respones['ClientShouldDo']['Skill']['ShouldEndConversation'] == 'Ture':
            text = self.d.WaitAnswer(respones['ClientShouldDo']['Skill']['RecordType'])
        else:
            pass
            
        
