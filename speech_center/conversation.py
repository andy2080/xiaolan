# -*- coding: utf-8 -*-
# 小蓝对话系统

# description:
# author: xiaoland
# create_time: 2018/7/9

"""
    desc:pass
"""

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
from Base import xiaolanBase


class dialogue(xiaolanBase):

    def __init__(self):

        super(dialogue, self).__init__()
    
    def conversation(self):

        """
        小蓝对话处理
        :return:
        """

        self.speaker('ding')
        self.recorder('Normal', 'a')
        self.speaker('dong')
        text = self.stt("./voice.wav")
        intentdict = self.client_to_server('NluReq', {'Text': text})
        self.client_to_server('SkillReq', {'Intent': intentdict['Intent'], 'Slots': intentdict['Slots'], 'IntentDict': intentdict})

    def waitAnswer(self, recordtype):

        """
        等待答案处理
        :param recordtype: 录制类型
        :return:
        """

        speaker.ding()
        if recordtype == 'ex':
            self.recorder.exrecord()
        elif recordtype == 'ts':
            self.recorder.tsrecord()
        elif recordtype == 's':
            self.recorder.srecord()
        elif recordtype == 'ss':
            self.recorder.ssrecord()
        else:
            self.recorder.record()
        speaker.dong()
        text = self.stt.stt("/home/pi/xiaolan/voice.wav", self.tok).replace('，', '').replace('。', '')
        text = self.replacenumber(text)
        if text == None or text == '':
            speaker.speacilrecorder()
        else:
            intentdict = self.xlnlu.xl_intent(text)
            if intentdict['intent'] == None or intentdict['intent'] == '':
                intentdict['skill'] = 'tuling'
            else:
                self.ClientToServer.ClientSkillResWaitAnswer(intentdict['intent'], intentdict['slots'], intentdict)

    def AskSlots(self, slotname, slotdicts, slotask, recordtype):

        """
        询问槽位信息处理
        :param slotname: 槽位名称
        :param slotdicts: 槽位字典
        :param recordtype: 录制类型
        :return:
        """
        a = 0
        slotturn = []
        while 1 == 1:
            if a < len(slotname) + 1:
                self.tts.tts(slotask[a], self.tok)
                speaker.speak()
                if recordtype[a] == 'normal':
                    self.recorder.record()
                elif recordtype[a] == 's':
                    self.recorder.srecord()
                elif recordtype[a] == 'ss':
                    self.recorder.ssrecord()
                elif recordtype[a] == 'ex':
                    self.recorder.exrecord()
                elif recordtype[a] == 'ts':
                    self.recorder.tsrecord()
                else:
                    self.recorder.record()
                text = self.stt.stt("./voice.wav", self.tok)
                text = self.replacenumber(text)
                slotturn.append(self.Nlu.get_slots([slotname[a], slotdicts[a]], text))
                a = a + 1
            else:
                break
        return slotturn

            
            
            
            
        
