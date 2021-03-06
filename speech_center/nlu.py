# -*- coding: utf-8 -*-

# description:
# author: xiaoland
# create_time: 2018/7/7

"""
    desc:pass
"""

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
sys.path.append('/home/pi/xiaolan/')
from Base import xiaolanBase

class Nlu(xiaolanBase):

        def __init__(self):

            super(Nlu, self).__init__()
            self.intentlist = self.datebase('Get', {'key': 'XiaolanIntentList', 'db': 'XiaolanSkill'})
            self.turn = 0
        
        def get_slots(self, slotslist, text):
            
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
                        if var['dict'][b] in text or var['same_means'][b] in text:
                                returndict['slotname'] = slotslist[a - 1]
                                returndict['value'] = var['dict'][b]
                        if len(var['dict']) == b:
                            a = a + 2
                            b = 0
                        else:
                            b = b + 1
            else:
                print('slots read error')
                self.log('write', {'log': "Slots Read Error", 'level': "error"})
                return returndict
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
                                'MainIntent': None,
                                'Intent': None,
                                'Skill': None,
                                'WordLexer': '',
                                'KeyWord': None,
                                'Commands': [
                                        'speaker', 'speacilrecorder'
                                ],
                                'States': [
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
                                'MainIntent': None,
                                'Intent': None,
                                'Skill': None,
                                'WordLexer': '',
                                'KeyWord': None,
                                'Commands': [
                                        'tts', '对不起，我无法理解您的意思'
                                ],
                                'States': [
                                        'nlu_intent_back_none'
                                ]
                        }
                except TypeError:
                        return {
                                'MainIntent': None,
                                'Intent': None,
                                'Skill': None,
                                'WordLexer': '',
                                'KeyWord':  None,
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
                                    'MainIntent': intent,
                                    'Intent': intent,
                                    'Skill': intent,
                                    'Commands': [
                                            'skills_requests'
                                    ],
                                    'States': [
                                        'nlu_intent_back_none'
                                    ]
                            }
                        else:
                            return {
                                    'MainIntent': None,
                                    'Intent': None,
                                    'Skill': None,
                                    'WordLexer': '',
                                    'KeyWord': None,
                                    'Commands': [
                                        'tts', '对不起，我无法理解您的意思'
                                    ],
                                    'States': [
                                        'nlu_intent_back_none'
                                    ]
                            }
                

        def xl_intent(self, text):

            b = 0
            a = 0
            c = 0
            data = {}
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
                    if var[b][c] in text:
                        slots = xlnlu.get_slots(self.intentlist[a][2], text)
                        data = {
                                'MainIntent': self.intentlist[a][0],
                                'Intent': self.intentlist[a][1][b],
                                'Skill': self.intentlist[a][3],
                                'Slots': slots,
                                'WordLexer': '',
                                'KeyWord': self.intentlist[a][2][b][c],
                                'Commands': [
                                        'skill', 'start'
                                ],
                                'States': [
                                        'xiaolan_nlu_intent_back'
                                ]
                        }
                        if len(var[b]) == c:
                            b = b + 1
                            c = 0
                        elif len(var) == b:
                            a = a + 1
                            b = 0
                            c = 0
                        elif len(self.intentlist) == a:
                            return data
                        else:
                            c = c + 1
                            
                if not data:
                    intent = self.ifly_intent(text)
                    return {
                            'MainIntent': intent,
                            'Intent': intent,
                            'Skill': intent,
                            'Slots': None,
                            'WordLexer': '',
                            'KeyWord': None,
                            'Commands': [
                                    'skill', 'start'
                            ],
                            'States': [
                                    'ifly_nlu_intent_back'
                            ]
                    }
                else:
                    return data
                
                
