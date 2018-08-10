# -*- coding: utf-8 -*-

import sys
import os
import json
import base64
import hashlib
import requests
import time
sys.path.append('/home/pi/xiaolan/')
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
            self.client_to_server('LogResForBrain', data)
        # ScreeDisplay&TextToSpeech
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
            RemindWord = respones['ClientShouldDo']['Skill']['ScreeDisplay']['RemindWord']
        elif Type == 'MusicDisplay':
            Title = respones['ClientShouldDo']['Skill']['ScreeDisplay']['Title']
            MusicUrl = respones['ClientShouldDo']['Skill']['ScreeDisplay']['MusicUrl']
            BackgroundImageUrl = respones['ClientShouldDo']['Skill']['ScreeDisplay']['BackgroundImageUrl']
            RemindWord = respones['ClientShouldDo']['Skill']['ScreeDisplay']['RemindWord']
        elif Type == 'ListDisplay':
            Title = respones['ClientShouldDo']['Skill']['ScreeDisplay']['Title']
            ListInfo = respones['ClientShouldDo']['Skill']['ScreeDisplay']['ListInfo']
            BackgroundImageUrl = respones['ClientShouldDo']['Skill']['ScreeDisplay']['BackgroundImageUrl']
            RemindWord = respones['ClientShouldDo']['Skill']['ScreeDisplay']['RemindWord']
        else:
            pass
        # OutputSpeech
        if not respones['ClientShouldDo']['Skill']['OutputSpeech'] or respones['ClientShouldDo']['Skill']['OutputSpeech'] == '':
            pass
        else:
            self.tts(respones['ClientShouldDo']['Skill']['OutputSpeech'])
        # AskSlots
        if not respones['ClientShouldDo']['Skill']['AskSlots'] or respones['ClientShouldDo']['Skill']['AskSlots'] == {}:
            pass
        else:
            slotsturn = self.dialogue('ask_slots', {'SlotNames': respones['ClientShouldDo']['Skill']['AskSlots']['SlotsName'], 'SlotDicts': respones['ClientShouldDo']['Skill']['AskSlots']['SlotsDict'], 'SlotAsks': respones['ClientShouldDo']['Skill']['AskSlots']['SlotsAsk'], 'RecordTypes': respones['ClientShouldDo']['Skill']['AskSlots']['RecordType']})
            self.client_to_server('SkillResForAskSlots', {'SkillName': respones['ClientShouldDo']['Skill']['SkillName'], 'Slots': slotsturn})
        # WaitAnswer
        if respones['ClientShouldDo']['Skill']['ShouldEndConversation'] == 'True':
            self.dialogue('conversation', {})
        else:
            pass
            
        
