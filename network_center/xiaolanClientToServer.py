# -*- coding: utf-8 -*-

import sys
import os
import json
import demjson
import requests
import hashlib
import base64
import time
sys.path.append('/home/pi/xiaolan/')
import setting
from Base import xiaolanBase

class ClientToServer(xiaolanBase):

    def __init__(self):

        super(ClientToServer, self).__init__()
        self.url = self.set['main_setting']['url']['xiaolanbrain']
    
    def DiyReq(self, data):
        
        r = requests.post(self.url,
                          data=data)
        return r.json()

    def XiaolanNluReq(self, text):

        """
        小蓝客户端发送给小蓝语义理解引擎HTTP请求
        :param text: 用户输入文本
        :return:
        """
        data = {
            'ClientEvent': {
                'Header': {
                    'NameSpace': 'xiaolan.client.requests.xiaolannlu',
                    'TimeStamp': time.time(),
                    'ClientId': self.set['main_setting']['ClientId'],
                    'ClientType': self.set['main_setting']['CLientType']
                },
            },
            'Info': {
                'Text': text,
            }
        }
        try:
            r = requests.post(self.set['main_setting']['url']['xiaolannlu'])
        except:
            return "Error:NluReqError"
        else:
            return r.json()

    def SkillAskSlotsRes(self, slotturn, skill):

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
                    'TimeStamp': time.time(),
                    'RequestsId': '7636',
                    'RequestsFrom': setting.setting()['main_setting']['ClientType'],
                    'ClientId': setting.setting()['main_setting']['ClientId']
                },
                'ConversationInfo': {
                    'ConversationId': None,
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
                'ClientId': setting.setting()['main_setting']['clientid'],
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
    
    def ClientSkillReq(self, intent, slots, intentdict):

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
                    'TimeStamp': int(time.time()),
                    'RequestsId': time.time(),
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
                        'SkillDate': self.set[intentdict['Skill']],
                        'Slots': slots
                    }
                }
            },
            'Debug': {
                'TimeStamp': str(int(time.time())),
                'ClientId': setting.setting()['main_setting']['clientid'],
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
        r = requests.post(self.url,
                          data=json.dumps(data))
        self.CommandsDo.Do(r.json())

    def ClientSkillResWaitAnswer(self, intent, slots, intentdict):

        """
        小蓝客户端发送给技能的waitanswer反馈
        shouldEndConversatiom为False的返回（waitAnswer为True）
        :param intent: 意图
        :param slots: 槽位
        :param intentdict: Nlu识别结果
        :return:
        """
    

