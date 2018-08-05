# -*- coding: utf-8 -*-
# 小蓝文字识别

# description:
# author: xiaoland
# create_time: 2018/8/3

"""
    desc:pass
"""

import sys
import os
import json
import requests
import base64
import urllib
import urllib2
sys.path.append('/home/pi/xiaolan/')
from Base import xiaolanBase

class XiaolanTextRecognition(xiaolanBase):

    def __init__(self):

        super(XiaolanTextRecognition, self).__init__()

    def get_token(self):

        """
        获取文字识别token
        :return:
        """
        apikey = self.set['main_setting']['OCR']['baidu']['AK']
        sercetkey = self.set['main_setting']['OCR']['baidu']['SK']
        url = 'http://openapi.baidu.com/oauth/2.0/token'
        params = urllib.urlencode({'grant_type': 'client_credentials',
                                   'client_id': apikey,
                                   'client_secret': sercetkey})
        r = requests.get(url, params=params)
        r.raise_for_status()
        token = r.json()['access_token']
        return token

    def baidu_text_recognition(self, img, token):

        """
        开始文字识别
        :param img: 图片
        :param token: token
        :return:
        """
        url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic?access_token=' + token
        f = open(img, "r")
        image = urllib.parse.quote(base64.b64encode(f.read()))
        data = {
            'image': image
        }

        r = requests.post(url,
                          data = data,
                          headers = {'Content-Type': 'application/x-www-form-urlencoded'})

        json = r.json()

        result_num = json['words_result_num']
        turn = 0
        word = 'a'
        while 1 == 1:
            if turn == result_num:
                break
            else:
                word = word + json['words_result'][turn]['words']
                turn += 1

        return {'States': 'Complete', 'Word': word}



