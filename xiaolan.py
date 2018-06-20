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
sys.path.append('/home/pi/xiaolan/speech_center')
import speaker

def welcome():
    
        print ('''

        ###################################
        #     小蓝--中文智能家居对话机器人     #
        #   (c)蓝之酱--1481605673@qq.com   #
        # www.github.com/xiaoland/xiaolan #
        #         欢迎使用!!!  :)           #
        ###################################

        ''')
        if setting.setting()['main_setting']['TTS']['service'] == 'baidu':
            stt = baidu_tts(1, 2, 3, 4)
            tok = tts.get_token()
        elif setting.setting()['main_setting']['TTS']['service'] == 'youdao':
            tts = youdao_tts()
            tok = setting.setting()['main_setting']['TTS']['youdao_tts']['lang']
        
        bt = baidu_tts()
        tok = bt.get_token()
        bt.tts(setting.setting()['main_setting']['your_name'] + '，你好啊，我是你的小蓝', tok)
        speaker.speak()
        os.system('pulseaudio --start')
        os.system('python /home/pi/xiaolan/auditory_center/awaken/snowboy.py')

welcome()
