# -*- coding: utf-8 -*-

import sys
import os
import json
import base64
import hashlib
import requests
import time
sys.path.append('/home/pi/xiaolan/')
from memory_center.Log import Log
import setting
from Base import xiaolanBase

class CommandsDo(xiaolanBase):
  
    def _init__(self):

        super(CommandsDo, self)._init__()

    def process(self, respones):

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
                            'ClientLog': self.log.Get("all")
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

            log = self.log('read', {'mode': 'all'})
            self.client_to_server('LogResForBrain')
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
            self.tts(respones['ClientShouldDo']['Skill']['OutputSpeech'])
        else:
            pass
        # AskSlots
        if respones['ClientShouldDo']['Skill']['AskSlots'] != None or respones['ClientShouldDo']['Skill']['AskSlots'] != {}:
            slotsturn = self.dialogue('ask_slots', {'SlotNames': respones['ClientShouldDo']['Skill']['AskSlots']['SlotsName'], 'SlotDicts': respones['ClientShouldDo']['Skill']['AskSlots']['SlotsDict'], 'SlotAsks': respones['ClientShouldDo']['Skill']['AskSlots']['SlotsAsk'], 'RecordTypes': respones['ClientShouldDo']['Skill']['AskSlots']['RecordType']})
            self.client_to_server('SkillResForAskSlots', {'SkillName': respones['ClientShouldDo']['Skill']['SkillName'], 'Slots': slotsturn})
        else:
            pass
        # WaitAnswer
        if respones['ClientShouldDo']['Skill']['ShouldEndConversation'] == 'Ture':
            text = self.dialogue('wait_answer', {'RecordType': respones['ClientShouldDo']['Skill']['RecordType']})
        else:
            pass
            
        
