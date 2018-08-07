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
import time
import threading
from Base import xiaolanBase
from speech_center.conversation import Dialogue

class Xiaolan(xiaolanBase):

    def __init__(self):

        super(Xiaolan, self).__init__()

    def awaken(self):

        """
        小蓝唤醒
        :return:
        """
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
        else:
            self.snowboy()

    def weather_remind(self):

        """
        小蓝天气提醒
        :return:
        """
        f = open('/home/pi/xiaolan/memory_center/more/face_track.txt', 'r')
        while 1 == 1:
            time.sleep(5)
            if int(f.read()) > 0 and time.strftime("%H") >= 18:
                self.log('write', {'log': 'Event:TomorrowWeatherRemind', 'level': 'info'})
                self.client_to_server('SkillReq', {'Intent': 'weather', 'Slots': {'time': 'tomorrow'}, 'IntengDict': {'Skill': 'Weather', 'KeyWord': 'remind', 'Text': '明天的天气怎么样？', 'WordLexer': {}}})
            elif int(f.read()) > 0 and time.strftime("%H") >= 5:
                if time.strftime("%H") <= 11:
                    self.log('write', {'log': 'Event:TodayWeatherRemind', 'level': 'info'})
                    self.client_to_server('SkillReq', {'Intent': 'weather', 'Slots': {'time': 'today'}, 'IntengDict': {'Skill': 'Weather', 'KeyWord': 'remind', 'Text': '今天天气怎么样？', 'WordLexer': {}}})
            elif not f.read():
                break
            else:
                pass
        f.close()

    def start(self):

        """
        启动小蓝
        :return:
        """
        print('''

        ###########################################
           小蓝——智能家居语音交互式人工智能机器人   
          https://www.github.com/xiaoland/xiaolan
            （c）2018袁翊闳——1481605673@qq.com
        ###########################################
        运行log请看/home/pi/xiaolan/memory_center/more/xiaolan.log
        
        ''')

        # 欢迎语
        self.log('write', {'log': 'Event:StartXiaolan', 'level': 'info'})
        self.tts(self.set['main_setting']['your_name'] + '，你好啊，我是你的小蓝')
        os.system('pulseaudio --start')
        self.awaken()

        """
        # 天气提醒与唤醒多线程并发
        threads = [];weather_remind = threading.Thread(target=Xiaolan.weather_remind, args=(self,));awaken = threading.Thread(target=Xiaolan.awaken, args=(self,));face_track = threading.Thread(target=Xiaolan.face_awaken, args=(self, 'face_track'))
        threads.append(weather_remind);threads.append(awaken);threads.append(face_track)
        weather_remind.start();awaken.start();face_track.start()
        for t in threads: t.join()
        """



x = Xiaolan()
d = Dialogue()

try:
    mode = sys.argv[1]
except IndexError:
    x.start()
else:
    if mode == 'unawaken':
        d.conversation()
    else:
        x.start()


