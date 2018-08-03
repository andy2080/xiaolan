# -*- coding: utf-8 -*-
# 小蓝手势识别

# description:
# author: xiaoland
# create_time: 2018/8/2

"""
    desc:pass
"""

import os
import sys
import json
import requests
import base64
sys.path.append('/home/pi/xiaolan/')
from Base import xiaolanBase


class Gesture(xiaolanBase):

    def __init__(self):

        super(Gesture, self).__init__()
        self.hands = ["unknown", "heart_a", "heart_b", "heart_c", "heart_d", "ok", "hand_open", "thumb_up",
                     "thumb_down", "rock", "namaste", "palm_up", "fist", "index_finger_up", "double_finger_up",
                     "victory", "big_v", "phonecall", "beg", " thanks"]

    def start(self, image):

        """
        手势识别
        :param image: 图片二进制文件
        :return:
        """
        info = {}
        trun = 0
        key = self.set['main_setting']['Gesture']['face++']['AK']
        sercet = self.set['main_setting']['Gesture']['face++']['AS']
        url = 'https://api-cn.faceplusplus.com/humanbodypp/beta/gesture'
        data = {
            'api_key': key,
            'api_secret': sercet,
            'image_base64': base64.b64encode(image)
        }

        r = requests.post(url,
                          body = data)

        json = r.json()

        try:
            json['error_message']
        except KeyError:
            info['States'] = 'Complete:XiaolanFace++GestureComplete'
            data = json['hands'][0]['gesture']
            while 1 == 1:
                if data[self.hands[trun]] > 79.9:
                    break
                else:
                    trun += 1

            hands = data[self.hands[trun]]
            info['Hands'] = hands
        else:
            info['States'] = 'Error:XiaolanFace++GestureError'
            info['Hand'] = None
        return info



