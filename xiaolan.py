# -*- coding: utf-8 -*-
# 小蓝中央控制

import sys
import os
import re
import setting
from speech_center.stt import baidu_stt
from speech_center.stt import ifly_stt
from speech_center.tts import baidu_tts
from speech_center.tts import youdao_tts
from Base import xiaolanBase
import speech_center.speaker as speaker
import visual_centre.face as face

class Xiaolan(xiaolanBase):

    def __init__(self):

        super(Xiaolan, self).__init__()

    def awaken(self):
    
        os.system('python /home/pi/xiaolan/auditory_center/awaken/snowboy.py')

    def welcome(self):
    
        print ('''

        ###################################
        #     小蓝--中文智能家居对话机器人     #
        #   (c)蓝之酱--1481605673@qq.com   #
        # www.github.com/xiaoland/xiaolan #
        #         欢迎使用!!!  :)           #
        ###################################

        ''')

        self.tts.tts(setting.setting()['main_setting']['your_name'] + '，你好啊，我是你的小蓝', tok)
        speaker.speak()
        os.system('pulseaudio --start')
        if self.set['main_setting']['awaken'] == 'hotword':
            self.awaken()
        elif self.set['main_setting']['awaken'] == 'face':
            face.awaken()
        elif self.set['main_setting']['awaken'] == 'all':
            pass

welcome()
