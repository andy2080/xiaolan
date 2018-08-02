# -*- coding: utf-8 -*-
# 小蓝中央控制

# description:
# author: xiaoland
# create_time: 2018/4/23

"""
    desc:pass
"""

import sys
import os
import re
from Base import xiaolanBase
from speech_center.conversation import Dialogue

class Xiaolan(xiaolanBase):

    def __init__(self):

        super(Xiaolan, self).__init__()

    def start(self):
    
        print ('''

        ###########################################
            小蓝——智能家居语音交互式人工智能机器人
          https://www.github.com/xiaoland/xiaolan
            （c）2018袁翊闳——1481605673@qq.com
        ###########################################
        运行log请看/home/pi/xiaolan/memory_center/more/xiaolan.log
        
        ''')

        self.log('write', {'log': 'Event:StartXiaolan', 'level': 'info'})
        self.tts(self.set['main_setting']['your_name'] + '，你好啊，我是你的小蓝')
        os.system('pulseaudio --start')
        if self.set['main_setting']['awaken'] == 'hotword':
            self.snowboy()
        elif self.set['main_setting']['awaken'] == 'face':
            f = open('./memory_center/more/first_start_xiaolan.txt', "r")
            if f.read() == '0':
                self.datebase('Set', {'date': ['XiaolanFaceUsers', []], 'db': 'XiaolanFace'})
                self.datebase('Set', {'date': ['XiaolanFaceUsersDate', {}], 'db': 'XiaolanFace'})
                self.face_awaken('all_new_sign_up')
                self.face_awaken('awaken')
            else:
                self.face_awaken('awaken')
        elif self.set['main_setting']['awaken'] == 'all':
            # thridings for two
            self.face_awaken('awaken')
            self.snowboy()

x = Xiaolan()
d = Dialogue()

try:
    mode = sys.argv[1]
except:
    x.start()
else:
    if mode == 'unawaken':
        d.conversation()
    else:
        x.start()


