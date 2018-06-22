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
            a = 1
            b = 1
            if len(slotslist) != None or slotslist != []:
                while self.turn == 0:
                    try:
                        var = slotslist[a]
                    except IndexError:
                        break
                    else:
                        if var['dict'][b] in text or var['same_means'] in text:
                                returndict[slotslist[a - 1]] = var['dict'][b]
                        else:
                            try:
                                varss = var['dict'][b]
                            except IndexError:
                                a = a + 1
                                b = 0
                            else:
                                b = b + 1
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
                                'commands': [
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
                                'commands': [
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
                                'commands': [
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
                                    'commands': [
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
                                    'commands': [
                                        'tts', '对不起，我无法理解您的意思'
                                    ],
                                    'states': [
                                        'nlu_intent_back_none'
                                    ]
                            }
                

        def xl_intent(self, text):

            b = 0
            a = 0
            xlnlu = Nlu()
            if self.turn == 0:
                while self.turn == 0:
                    try:
                        var = [a][1]
                    except IndexError:
                        data = None
                        break
                    else:
                        pass
                    if var[b] in text:
                        slots = xlnlu.get_slots(self.intentlist[a][2], text)
                        data = {
                                'intent': self.intentlist[a][0][b],
                                'skill': self.intentlist[a][3],
                                'slots': slots,
                                'commands': [
                                        'skill', 'start'
                                ]
                                'states': [
                                        'xiaolan_nlu_intent_back'
                                ]
                        }
                    else:
                        try:
                            varss = var[b]
                        except IndexError:
                            a = a + 1
                            b = 0
                        else:
                            b = b + 1
                if data == None:
                    return {
                            'intent': xlnlu.ifly_intent(text),
                            'skill': xlnlu.ifly_intent(text),
                            'slots': None,
                            'commands': [
                                    'skill', 'start'
                            ]
                            'states': [
                                    'ifly_nlu_intent_back'
                            ]
                    }
                else:
                    return data
                
                
