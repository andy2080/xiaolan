# -*- coding: utf-8 -*-
# 小蓝对话系统

# description:
# author: xiaoland
# create_time: 2018/8/3

"""
    desc:pass
"""
import json
import requests
import sys
import os
import base64
sys.path.append('/home/pi/xiaolan/')
from Base import xiaolanBase

class HumanBodyTrack(xiaolanBase):

    def __init__(self):

        super(HumanBodyTrack, self).__init__()

    def get_token(self):

        """
        获取人体识别token
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

    def body_keyplace_track(self, img, token):

        """
        百度人体关键点检测
        :param img: 检测图片路径
        :param token: token
        :return:
        """
        url = 'https://aip.baidubce.com/rest/2.0/image-classify/v1/body_analysis?access_token=' + token
        f = open(img, "r")
        image = base64.b64encode(f.read())
        f.close()
        data = {
            'image': image
        }

        r = requests.post(url,
                          data = data,
                          headers = {'Content-Type': 'application/x-www-form-urlencoded'})

        json = r.json()

        return {'States': 'Complete', 'Data': json}
