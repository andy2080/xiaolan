# -*- coding: utf-8 -*-
# 小蓝对话系统
import sys
import os
import re
import speaker
from tts import baidu_tts
from tts import youdao_tts
from stt import baidu_stt
from stt import ifly_stt
from nlu import Nlu
sys.path.append('/home/pi/xiaolan/')
from auditory_center.recorder import recorder
from network_center.xiaolanClientToServer import ClientToServer
import setting


class dialogue(object):
    def __init__(self):
        bt = baidu_tts()
        if setting.setting()['main_setting']['STT']['service'] == 'baidu':
            self.stt = baidu_stt(1, 2, 3, 4)
            self.tok = self.stt.get_token()
        elif setting.setting()['main_setting']['STT']['service'] == 'ifly':
            self.stt = ifly_stt()
            self.tok = 1
        if setting.setting()['main_setting']['TTS']['service'] == 'baidu':
            self.tts = baidu_tts()
            self.tok = self.tts.get_token()
        elif setting.setting()['main_setting']['TTS']['service'] == 'youdao':
            self.tts = youdao_tts()
            self.tok = setting.setting()['main_setting']['TTS']['youdao_tts']['lang']
        self.xlnlu = Nlu()
        self.r = recoder()
        self.b = 0
    def replacenumber(self, text):
        try:
            text.replace('零', 0)
            text.replace('一', 1)
            text.replace('二', 2)
            text.replace('三', 3)
            text.replace('四', 4)
            text.replace('五', 5)
            text.replace('六', 6)
            text.replace('七', 7)
            text.replace('八', 8)
            text.replace('九', 9)
        except TypeError:
            return text
        except KeyError:
            return text
        else:
            return text
        
    
    def conversationa(self):

        d = dialogue()
        speaker.ding()
        self.r.record()
        speaker.dong()
        text = self.stt.stt("/home/pi/xiaolan/voice.wav", self.tok).replace('，', '').replace('。', '')
        text = d.replacenumber(text)
        if text == None or text == '':
            speaker.speacilrecorder()
        else:
            intentdict = self.xlnlu.xl_intent(text)
            sk = skills()
            sk.ClientReq(intentdict['skillurl'], intentdict['intent'], intentdict['slots'], intentdict)

    def conversationb(self):

        d = dialogue()
        speaker.ding()
        self.r.record()
        speaker.dong()
        text = self.stt.stt("/home/pi/xiaolan/voice.wav", self.tok).replace('，', '').replace('。', '')
        text = d.replacenumber(text)
        if text == None or text == '':
            speaker.speacilrecorder()
        else:
            return text

    def AskSlots(self, slotname, slotdicts, recordtype):
        
        d = dialogue()
        self.tts(ask, self.tok)
        speaker.speak()
        speaker.ding()
        if recordtype == 'ex':
            r.exrecord()
        elif recordtype == 'ts':
            r.tsrecord()
        elif recordtype == 's':
            r.srecord()
        elif recordtype == 'ss':
            r.ssrecord()
        else:
            r.record()
        speaker.dong()
        text = self.stt.stt("/home/pi/xiaolan/voice.wav", self.tok).replace('，', '').replace('。', '')
        text = d.replacenumber(text)
        slotlist = []
        a = 0
        while self.b == 0:
            slotlist.append(slotname[a])
            slotlist.append(slotdicts[a])
            if len(slotdicts) == a:
                break
            else:
                a = a + 1
            
        return {
            'slots': self.xlnlu.get_slots(slotlist, text),
            'text': text
            }

    def tts_text(text, service, more):

        if service == 'baidu':
            tts = baidu_tts()
            tts.tts(text, self.token)
            speaker.speak()
        elif service == 'youdao':
            tts = youdao_tts()
            tts.tts(text, more)
        else:
            self.tts.tts(text, self.tok)
            
            
            
            
        
