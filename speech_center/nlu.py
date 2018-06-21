# -*- coding: utf-8 -*-

import sys
if sys.getdefaultencoding() != 'utf-8':
        reload(sys)
        sys.setdefaultencoding('utf-8')
import time
import os
import json
import requests
import demjson
import base64
import hashlib
from tts import baidu_tts
from stt import baidu_stt
from stt import ifly_stt
from tts import youdao_tts
sys.path.append('/home/pi/xiaolan/')
from auditory_center.recorder import recorder
sys.path.append('/home/pi/xiaolan/memory_center')
import intentlist

class Nlu(object):
        def __init__(self):
                self.intentlist = intentlist.intentlistturn()
                self.turn = 0
        
        def get_slots(slotslist, text):
            
            returndict = {}
            a = 0
            b = 1
            c = 0
            try:
                if len(slotslist) != None or len(slotslist) != []:
                    while self.turn == 0:
                        if slotslist[b]['dict'][a] in text or slotslist[b]['same_means'][a] in text:
                            returndict[slotslist[c]] = slotslist[b]['dict'][a]
                            if len(slotslist) == b:
                                break
                            else:
                                b = b + 2
                                c = c + 2
                        else:
                            a = a + 1
                else:
                    return returndict
                return returndict
            except KeyError:
                return returndict
                        
        def ifly_intent(self, text):
                
                appid = self.selfset['main_setting']['NLU']['ifly']['appid']
                apikey = self.selfset['main_setting']['NLU']['ifly']['key']
                curtimeo = int(time.time())
                curtimef = str(curtimeo)
        
                try:
                        textl = base64.b64encode(text)
                except TypeError:
                        return {
                                'intent': None,
                                'skill': None,
                                'command': [
                                        'speaker', 'speacilrecorder'
                                ],
                                'states': [
                                        'nlu_intent_back_none'
                                ]
                        }
        
                csumc = apikey + curtimef + 'eyJ1c2VyaWQiOiIxMyIsInNjZW5lIjoibWFpbiJ9' + 'text=' + textl

                c = hashlib.md5()
                c.update(csumc)
                checksuml = c.hexdigest()
        
                headers = {'X-Appid': appid, 'Content-type': 'application/x-www-form-urlencoded; charset=utf-8', 'X-CurTime': curtimef, 'X-Param': 'eyJ1c2VyaWQiOiIxMyIsInNjZW5lIjoibWFpbiJ9', 'X-CheckSum': checksuml}
                url = 'http://api.xfyun.cn/v1/aiui/v1/text_semantic?text=' + textl
        
                r = requests.post(url,
                                  headers=headers)
                json = r.json()
                try:
                        intent = json['data']['service']
                except KeyError:
                        return {
                                'intent': None,
                                'skill': None,
                                'command': [
                                        'tts', '对不起，我无法理解您的意思'
                                ],
                                'states': [
                                        'nlu_intent_back_none'
                                ]
                        }
                except TypeError:
                        return {
                                'intent': None,
                                'skill': None,
                                'command': [
                                        'tts', '对不起，我无法理解您的意思'
                                ],
                                'states': [
                                        'nlu_intent_back_none'
                                ]
                                        
                        }
                else:
                        if intent != None or intent != '':
                            return {
                                    'intent': intent,
                                    'skill': intent,
                                    'command': [
                                            'skills_requests'
                                    ],
                                    'states': [
                                        'nlu_intent_back_none'
                                    ]
                            }
                        else:
                            return {
                                    'intent': None,
                                    'skill': None,
                                    'command': [
                                        'tts', '对不起，我无法理解您的意思'
                                    ],
                                    'states': [
                                        'nlu_intent_back_none'
                                    ]
                            }
                

        def xl_intent(self, text):

            b = 0
            a = 0
            c = 0
            try:
                while self.turn == 0:
                    
                        if self.intentlist[b][1][a] in text:
                                if self.intentlist[b][2] != [] or self.intentlist[b][1] != None:
                                        slots = self.xlnlu.get_slots(self.intentlist[b][2], text)
                                else:
                                        slots = None
                                returndict = {
                                        'intent': self.intentlist[b][0][a][c],
                                        'skill': self.intentlist[b][3],
                                        'slots': slots,
                                        'text': text,
                                        'command': [
                                                'skill', 'start'
                                        ],
                                        'states': [
                                                'xl_nlu_intent_back'
                                        ]
                                }
                                break
                        else:
                                b = b + 1
                                a = a + 1
                                c = c + 1
                return returndict
            except KeyError:
                return {
                        'intent': self.xlnlu.ifly_intent(text),
                        'skill': self.xlnlu.ifly_intent(text),
                        'slots': None,
                        'commmands': [
                                'skill', 'start'
                        ],
                        'states': [
                                'ifly_nlu_intent_back'
                        ]
                }
