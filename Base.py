# -*- coding: utf-8 -*-

import os
import sys
import json
import requests
import setting
from memory_center.Log import Log
from memory_center.DateBase import DateBase
from speech_center.stt import baidu_stt
from speech_center.stt import ifly_stt
from speech_center.tts import baidu_tts
from speech_center.tts import youdao_tts
from speech_center.conversation import dialogue
from speech_center.nlu import Nlu
from network_center.xiaolanClientToServer import ClientToServer
from network_center.xiaolanServerCommandDo import CommandsDo
from auditory_center.recorder import recorder
from auditory_center.awaken.snowboy import snowboy



class xiaolanBase(object):

    def __init__(self):

        self.set = setting.setting()
        self.Log = Log()
        self.Datebase = DateBase()
        self.dialogue = dialogue()
        self.recorder = recorder()
        self.snowboy = snowboy()
        self.Nlu = Nlu()
        self.ClientToServer = ClientToServer()
        self.CommandsDo = CommandsDo()
        if self.set['main_setting']['TTS']['service'] == 'baidu':
            self.tts = baidu_tts()
            self.tok = self.tts.get_token()
        elif self.set['main_setting']['TTS']['service'] == 'youdao':
            self.tts = youdao_tts()
            self.tok = self.set['main_setting']['TTS']['youdao']['lang']
        elif self.set['main_setting']['STT']['service'] == 'baidu':
            self.stt = baidu_stt()
            self.tok = self.stt.get_token()
        elif self.set['main_setting']['STT']['service'] == 'ifly':
            self.stt = ifly_stt()
            self.tok = ''
