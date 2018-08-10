# -*- coding: utf-8 -*-

# description:
# author: xiaoland
# create_time: 2018/7/7

"""
    desc:pass
"""

import sys
import os
import json
import demjson
import requests
import hashlib
import base64
import time
sys.path.append('/home/pi/xiaolan/')
from Base import xiaolanBase

class ClientToServer(xiaolanBase):

    def __init__(self):

        super(ClientToServer, self).__init__()
        self.brainurl = self.set['main_setting']['url']['xiaolan_brain'] + ':8000'
        self.nluurl = self.set['main_setting']['url']['xiaolan_nlu'] + ':8000'
    
    def diy_req(self, data):
        
        r = requests.post(self.brainurl,
                          data=data)
        return r.json()

    def xiaolan_nlu_req(self, text):

        """
        小蓝客户端发送给小蓝语义理解引擎HTTP请求
        :param text: 用户输入文本
        :return:
        """
        data = {
            'ClientEvent': {
                'Header': {
                    'NameSpace': 'xiaolan.client.requests.xiaolannlu.process',
                    'TimeStamp': str(int(time.time())),
                    'ClientId': self.set['main_setting']['ClientId'],
                    'ClientType': self.set['main_setting']['ClientType']
                },
            },
            'Info': {
                'Text': text,
            }
        }
        data = json.dumps(data)
        try:
            r = requests.post(self.nluurl,
                              data = data)
        except requests.exceptions.HTTPError:
            return "Error:NluReqError"
        else:
            return r.json()

    def skill_ask_slots_res(self, slotturn, skill):

        """
        小蓝客户端发送给技能的槽位信息反馈
        :param slotturn: 槽位
        :param skill: 技能
        :return:
        """
        data = {
            'ClientEvent': {
                'Header': {
                    'NameSpace': 'xiaolan.client.respones.skill.askslots',
                    'TimeStamp': str(int(time.time())),
                    'RequestsId': '7636',
                    'RequestsFrom': setting.setting()['main_setting']['ClientType'],
                    'ClientId': setting.setting()['main_setting']['ClientId']
                },
                'ConversationInfo': {
                    'ConversationId': '674536876453',
                    'ShouldHandlerSkill': skill,
                    'SkillShouldHandler': None,
                    'SkillAwakenKeyword': None,
                    'SendToSkillInfo': {
                        'Intent': None,
                        'Text': None,
                        'SkillDate': None,
                        'Slots': slotturn
                    }
                }
            },
            'Debug': {
                'TimeStamp': str(int(time.time())),
                'ClientId': setting.setting()['main_setting']['ClientId'],
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
        try:
            r = requests.post(self.brainurl,
                              data=data)
        except requests.exceptions.HTTPError:
            return {'States': 'Error:Unknow...'}
        else:
            json = r.json()
            json['States'] = 'Complete'
            return json
    
    def client_skill_req(self, intent, slots, intentdict):

        """
        小蓝客户端发送给技能的请求
        :param intent: 意图
        :param slots: 槽位
        :param intentdict: Nlu识别结果
        :return:
        """
        data = {
            'ClientEvent': {
                'Header': {
                    'NameSpace': 'xiaolan.client.requests.user.skill.need',
                    'TimeStamp': str(int(time.time())),
                    'RequestsId': base64.b64encode(int(time.time())),
                    'RequestsFrom': setting.setting()['main_setting']['ClientType'],
                    'ClientId': setting.setting()['main_setting']['ClientId']
                },
                'ConversationInfo': {
                    'ConversationId': '456564889456',
                    'ShouldHandlerSkill': intentdict['Skill'],
                    'SkillShouldHandler': intent,
                    'SkillAwakenKeyword': intentdict['KeyWord'],
                    'SendToSkillInfo': {
                        'Intent': intent,
                        'WordLexer': intentdict['WordLexer'],
                        'Text': intentdict['Text'],
                        'Slots': slots
                    }
                }
            },
            'Debug': {
                'TimeStamp': str(int(time.time())),
                'ClientId': setting.setting()['main_setting']['ClientId'],
                'States': {
                    'ClientStates': ['servicing'],
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
        r = requests.post(self.brainurl,
                          data=json.dumps(data))
        self.commands_do('Normal', {'Respones': r.json()})

    def client_skill_res_wait_answer(self, intent, slots, intentdict):

        """
        小蓝客户端发送给技能的waitanswer反馈
        shouldEndConversation为False的返回（waitAnswer为True）
        :param intent: 意图
        :param slots: 槽位
        :param intentdict: Nlu识别结果
        :return:
        """

    def log_res_for_brain(self, log):

        """
        log返回给brain
        :param log: log
        :return:
        """
        data = {
            'ClientEvent': {
                'Header': {
                    'NameSpace': 'xiaolan.client.respones.client.log',
                    'TimeStamp': str(int(time.time())),
                    'RequestsId': time.time(),
                    'RequestsFrom': setting.setting()['main_setting']['ClientType'],
                    'ClientId': setting.setting()['main_setting']['ClientId']
                },
                'ConversationInfo': None
            },
            'Debug': {
                'TimeStamp': str(int(time.time())),
                'Log': log,
                'ClientId': setting.setting()['main_setting']['ClientId'],
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
        r = requests.post(self.brainurl,
                          data=json.dumps(data))
        return {'States': r.json()['Debug']['States']}


    def get_remind_word(self):

        """
        获取提醒词
        :return:
        """
        data = {
            'ClientEvent': {
                'Header': {
                    'NameSpace': 'xiaolan.client.requests.get.remindword.normal',
                    'TimeStamp': int(time.time()),
                    'RequestsId': time.time(),
                    'RequestsFrom': setting.setting()['main_setting']['ClientType'],
                    'ClientId': setting.setting()['main_setting']['ClientId']
                },
                'ConversationInfo': None
            },
            'Debug': {
                'TimeStamp': str(int(time.time())),
                'ClientId': setting.setting()['main_setting']['ClientId'],
                'States': {
                    'ClientStates': ['servicing'],
                    'NluStates': ['working'],
                    'SttStates': ['working'],
                    'TtsStates': ['emptying']
                },
                'Commands': {
                    'ClientCommands': ['servicing for user'],
                    'elseCommands': []
                }
            }
        }
        r = requests.post(self.brainurl,
                          data=json.dumps(data))
        return {'States': r.json()['Debug']['States'], 'RemindWord': r.json()['BrainEvent']['Respones']['RemindWord']}

    def get_recommend_word(self):

        """
        获取推荐词
        :return:
        """
        data = {
            'ClientEvent': {
                'Header': {
                    'NameSpace': 'xiaolan.client.requests.get.recommendword',
                    'TimeStamp': int(time.time()),
                    'RequestsId': time.time(),
                    'RequestsFrom': setting.setting()['main_setting']['ClientType'],
                    'ClientId': setting.setting()['main_setting']['ClientId']
                },
                'ConversationInfo': None
            },
            'Debug': {
                'TimeStamp': str(int(time.time())),
                'ClientId': setting.setting()['main_setting']['ClientId'],
                'States': {
                    'ClientStates': ['servicing'],
                    'NluStates': ['working'],
                    'SttStates': ['working'],
                    'TtsStates': ['emptying']
                },
                'Commands': {
                    'ClientCommands': ['servicing for user'],
                    'elseCommands': []
                }
            }
        }
        r = requests.post(self.brainurl,
                          data=json.dumps(data))
        return {'States': r.json()['Debug']['States'], 'RemindWord': r.json()['BrainEvent']['Respones']['RecommendWord']}


    def get_weather_remind__word(self):

        """
        获取天气提醒词
        :return:
        """
        data = {
            'ClientEvent': {
                'Header': {
                    'NameSpace': 'xiaolan.client.requests.get.remindword.weather',
                    'TimeStamp': int(time.time()),
                    'RequestsId': time.time(),
                    'RequestsFrom': setting.setting()['main_setting']['ClientType'],
                    'ClientId': setting.setting()['main_setting']['ClientId']
                },
                'ConversationInfo': None
            },
            'Debug': {
                'TimeStamp': str(int(time.time())),
                'ClientId': setting.setting()['main_setting']['ClientId'],
                'States': {
                    'ClientStates': ['servicing'],
                    'NluStates': ['working'],
                    'SttStates': ['working'],
                    'TtsStates': ['emptying']
                },
                'Commands': {
                    'ClientCommands': ['servicing for user'],
                    'elseCommands': []
                }
            }
        }
        r = requests.post(self.brainurl,
                          data=json.dumps(data))
        return {'States': r.json()['Debug']['States'], 'RemindWord': r.json()['BrainEvent']['Respones']['RemindWord']}

    def get_recommend_skill(self):

        """
        获取推荐技能
        :return:
        """
        data = {
            'ClientEvent': {
                'Header': {
                    'NameSpace': 'xiaolan.client.requests.get.recommendskill',
                    'TimeStamp': int(time.time()),
                    'RequestsId': time.time(),
                    'RequestsFrom': setting.setting()['main_setting']['ClientType'],
                    'ClientId': setting.setting()['main_setting']['ClientId']
                },
                'ConversationInfo': None
            },
            'Debug': {
                'TimeStamp': str(int(time.time())),
                'ClientId': setting.setting()['main_setting']['ClientId'],
                'States': {
                    'ClientStates': ['servicing'],
                    'NluStates': ['working'],
                    'SttStates': ['working'],
                    'TtsStates': ['emptying']
                },
                'Commands': {
                    'ClientCommands': ['servicing for user'],
                    'elseCommands': []
                }
            }
        }
        r = requests.post(self.brainurl,
                          data=json.dumps(data))
        return {'States': r.json()['Debug']['States'], 'RecommendSkill': r.json()['BrainEvent']['Respones']['RecommendSkill']}