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
import threading
from tts import baidu_tts
from tts import youdao_tts
from stt import baidu_stt
from stt import ifly_stt
from nlu import Nlu
sys.path.append('/home/pi/xiaolan/')
from Base import xiaolanBase


class Dialogue(xiaolanBase):

    def __init__(self):

        super(Dialogue, self).__init__()
    
    def conversation(self):

        """
        小蓝对话处理
        :return:
        """

        self.speaker('ding')
        threads = [];stt = threading.Thread(self.stt, ("/home/pi/xiaolan/voice.wav",));record = threading.Thread(self.recorder, ('normal', 0))
        threads.append(stt);threads.append(record)
        stt.start();record.start()
        for t in threads: t.join()
        self.speaker('dong')
        f = open('/home/pi/xiaolan/memory_center/more/text.txt', "r");text = f.read();f.close()
        intentdict = self.client_to_server('NluReq', {'Text': text})
        self.client_to_server('SkillReq', {'Intent': intentdict['Intent'], 'Slots': intentdict['Slots'], 'IntentDict': intentdict})

    def wait_answer(self, recordtype):

        """
        等待答案处理
        :param recordtype: 录制类型
        :return:
        """

        self.speaker('ding')
        if recordtype == 'ex':
            self.recorder('express', 0)
        elif recordtype == 'normal':
            self.recorder('normal', 0)
        elif recordtype == 'ts':
            self.recorder('translate', 0)
        elif recordtype == 's':
            self.recorder('less_time', 0)
        else:
            self.recorder('normal', 0)
        self.speaker('dong')
        text = self.stt("/home/pi/xiaolan/voice.wav")
        intentdict = self.client_to_server('NluReq', {'Text': text})
        self.client_to_server('SkillResForWaitAnswer', {'Intent': intentdict['intent'], 'Slots': intentdict['slots'], 'IntentDict': intentdict})

    def ask_slots(self, slotname, slotdicts, slotask, recordtype):

        """
        询问槽位信息处理
        :param slotname: 槽位名称
        :param slotdicts: 槽位字典
        :param recordtype: 录制类型
        :param slotask: 槽位询问语句
        :return:
        """
        a = 0
        slotturn = []
        while 1 == 1:
            if a < len(slotname) + 1:
                self.tts(slotask[a])
                if recordtype[a] == 'normal':
                    self.recorder('normal', 0)
                elif recordtype[a] == 's':
                    self.recorder('less_time', 0)
                elif recordtype[a] == 'ex':
                    self.recorder('express', 0)
                elif recordtype[a] == 'ts':
                    self.recorder('translate', 0)
                else:
                    self.recorder.record()
                text = self.stt("/home/pi/xiaolan/voice.wav")
                slotturn.append(self.client_nlu('get_slots', {'Text': text, 'SlotsList': [slotname[a], slotdicts[a]]}))
                a = a + 1
            else:
                break
        return slotturn

            
            
            
            
        
