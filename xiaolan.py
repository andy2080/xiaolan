# -*- coding: utf-8 -*-
# 小蓝中央控制

# description:
# author: xiaoland
# create_time: 2018/4/23

"""
    desc:pass
"""

import sys

sys.setrecursionlimit(1000000)

import os
import re
import setting
from speech_center.stt import baidu_stt
from speech_center.stt import ifly_stt
from speech_center.tts import baidu_tts
from speech_center.tts import youdao_tts
from Base import xiaolanBase
import speech_center.speaker as speaker

class Xiaolan(xiaolanBase):

    def __init__(self):

        super(Xiaolan, self).__init__()

    def start(self):
    
        print ('''

        #############################################
        #       小蓝——语音交互式智能家居机器人        #  
        #  https://www.github.com/xiaoland/xiaolan   #
        #    （c）2018袁翊闳——1481605673@qq.com     #
        #############################################
        
        ''')

        self.tts(self.set['main_setting']['your_name'] + '，你好啊，我是你的小蓝')
        speaker.speak()
        os.system('pulseaudio --start')
        if self.set['main_setting']['awaken'] == 'hotword':
            self.snowboy()
        elif self.set['main_setting']['awaken'] == 'face':
            try:
                f = open('./memory_center/face_img/face_datebase/main.jpg')
            except:
                self.face_awaken('all_new_sign_up')
            finally:
                self.face_awaken('awaken')
        elif self.set['main_setting']['awaken'] == 'all':
            # thridings for two
            self.face_awaken('awaken')
            self.snowboy()

x = Xiaolan()
x.start()
