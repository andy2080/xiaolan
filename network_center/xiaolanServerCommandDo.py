# -*- coding: utf-8 -*-

import sys
import os
import json
import base64
import hashlib
import requests
import time
# from xiaolanClientToServer import ClientToServer
sys.path.append('/home/pi/xiaolan/')
from memory_center.Log import Log
import setting
# from memory_center.log import Log
# from memory_center.commandlist import clist
from speech_center.tts import baidu_tts
from speech_center.tts import youdao_tts

class CommandsDo(object):
  
    def _init__(self):
        self.url = ''
        self.xscd = CommandsDo()
        self.l = Log()
        if setting.setting()['main_setting']['TTS']['service'] == 'baidu':
            self.tts = baidu_tts()
            self.token = self.tts.get_token()
        elif setting.setting()['main_setting']['TTS']['service'] == 'youdao':
            self.tts = youdao_tts()
            self.token = setting.setting()['main_setting']['TTS']['youdao']['lang']
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
                                'NameSpace': 'xiaolan.client.send.ClientLog',
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
                            'ClientLog': self.l.Get()
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
            r = requests.post(self.url,
                              data=data)
        # ScreeDisplay
        Type = respones['ClientShouldDo']['Skill']['ScreeDisplay']['Type']
        if Type == 'TextDisplay':
            Title = respones['ClientShouldDo']['Skill']['ScreeDisplay']['Title']
            Text = respones['ClientShouldDo']['Skill']['ScreeDisplay']['Text']
            BackgroundImageUrl = respones['ClientShouldDo']['Skill']['ScreeDisplay']['BackgroundImageUrl']
            Remind = respones['ClientShouldDo']['Skill']['ScreeDisplay']['RemindWord']
        elif Type == 'ImageDisplay':
            Title = respones['ClientShouldDo']['Skill']['ScreeDisplay']['Title']
            ImageUrl = respones['ClientShouldDo']['Skill']['ScreeDisplay']['ImageUrl']
            BackgroundImageUrl = respones['ClientShouldDo']['Skill']['ScreeDisplay']['BackgroundImageUrl']
            RemindWord = respones['ClientShouldDo']['Skill']['ScreeDisplay']['RemindWord']
        elif Type == 'VideoDisplay':
            Title = respones['ClientShouldDo']['Skill']['ScreeDisplay']['Title']
            VideoUrl = respones['ClientShouldDo']['Skill']['ScreeDisplay']['VideoUrl']
            BackgroundImageUrl = respones['ClientShouldDo']['Skill']['ScreeDisplay']['BackgroundImageUrl']
            RemindWord = respones['ClientShouldDo']['Skill']['ScreeDisplay']['RemindWord']
        elif Type == 'MusicDisplay':
            Title = respones['ClientShouldDo']['Skill']['ScreeDisplay']['Title']
            MusicUrl = respones['ClientShouldDo']['Skill']['ScreeDisplay']['MusicUrl']
            BackgroundImageUrl = respones['ClientShouldDo']['Skill']['ScreeDisplay']['BackgroundImageUrl']
            RemindWord = respones['ClientShouldDo']['Skill']['ScreeDisplay']['RemindWord']
        else:
            pass
        # OutputSpeech
        if respones['ClientShouldDo']['Skill']['OutputSpeech'] != None or respones['ClientShouldDo']['Skill']['OutputSpeech'] != '':
            self.tts.tts(respones['ClientShouldDo']['Skill']['OutputSpeech'], self.token)
        else:
            pass
        # AskSlots
        if respones['ClientShouldDo']['Skill']['AskSlots'] != None or respones['ClientShouldDo']['Skill']['AskSlots'] != {}:
            slotsturn = self.f.AskSlots(respones['ClientShouldDo']['Skill']['AskSlots']['SlotsName'], respones['ClientShouldDo']['Skill']['AskSlots']['SlotsDict'], respones['ClientShouldDo']['Skill']['AskSlots']['SlotsAsk'], respones['ClientShouldDo']['Skill']['AskSlots']['RecordType'])
            self.xscd.SkillAskSlotsRes(slotsturn)
        else:
            pass
        # WaitAnswer
        if respones['ClientShouldDo']['Skill']['ShouldEndConversation'] == 'Ture':
            text = self.d.waitAnswer(respones['ClientShouldDo']['Skill']['RecordType'])
        else:
            pass
            
        
