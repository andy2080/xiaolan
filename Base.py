# -*- coding: utf-8 -*-

# description:
# author: xiaoland
# create_time: 2018/7/19

"""
    desc:pass
"""

import os
import sys
import json
import requests

class xiaolanBase(object):

    def __init__(self):

        import setting
        self.set = setting.setting()
        from visual_centre.face import XiaolanFaceAwaken
        self.face_awaken = XiaolanFaceAwaken()
        from memory_center.Log import Log
        self.Log = Log()
        from memory_center.DateBase import DateBase
        self.Datebase = DateBase()
        from speech_center.conversation import dialogue
        self.dialogue = dialogue()
        from auditory_center.recorder import recorder
        self.recorder = recorder()
        from auditory_center.awaken.snowboy import snowboy
        self.snowboy = snowboy()
        from speech_center.nlu import Nlu
        self.Nlu = Nlu()
        from network_center.xiaolanClientToServer import ClientToServer
        self.ClientToServer = ClientToServer()
        from network_center.xiaolanServerCommandDo import CommandsDo
        self.CommandsDo = CommandsDo()
        from learning_center.SpeacilSkills import SpeacilSkills
        self.SpeacilSkills = SpeacilSkills()
        from speech_center.stt import baidu_stt
        from speech_center.stt import ifly_stt
        from speech_center.tts import baidu_tts
        from speech_center.tts import youdao_tts
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
