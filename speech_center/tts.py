# -*- coding: utf-8 -*-
# TTS

# description:
# author: xiaoland
# create_time: 2018/4/21

"""
    desc:pass
"""

import sys
import os
import logging
import requests
import wave
import json
import pyaudio
import time
import shutil
import urllib2
import urllib
import base64
import md5
import random
import tempfile
from urllib import quote
sys.path.append('/home/pi/xiaolan/')
import setting
from Base import xiaolanBase
sys.path.append('/home/pi/xiaolan/speech_center')
import speaker

class baidu_tts(xiaolanBase):

    def __init__(self):
        
        super(baidu_tts, self).__init__()
        
    def get_token(self):

        AK = self.set['main_setting']['TTS']['baidu']['AK']
        SK = self.set['main_setting']['TTS']['baidu']['SK']
        URL = 'http://openapi.baidu.com/oauth/2.0/token'
        
        params = urllib.urlencode({'grant_type': 'client_credentials',
                                   'client_id': AK,
                                   'client_secret': SK})
        r = requests.get(URL, params=params)
        try:
            r.raise_for_status()
            token = r.json()['access_token']
            return token
        except requests.exceptions.HTTPError:
            self._logger.critical('Token request failed with response: %r',
                                  r.text,
                                  exc_info=True)
          
        
    def tts(self, saytext, token):

        data = {'tex': saytext,
                 'lan': 'zh',
                 'tok': token,
                 'ctp': 1,
                 'cuid': 'b0-10-41-92-84-4d',
                 'per': 4
                 }
        r = requests.post('http://tsn.baidu.com/text2audio',
                          data=data,
                          headers={'content-type': 'application/json'},stream=True)

        if r.status_code == 200:
            with open(r"/home/pi/xiaolan/memory_center/musiclib/say.mp3", 'wb') as f:  
                r.raw.decode_content = True  
                shutil.copyfileobj(r.raw, f)
                return {'States': 'BaiduTTSComplete'}
        else:
            self.tts('对不起，我的语言中枢出错了，我不能跟你说话了', token)
            speaker.speak()
            return {'States': 'Error:BaiduTTSError'}

class youdao_tts(xiaolanBase):
    
    def __init__(self):
        
        super(youdao_tts, self).__init__()
    
    def tts(self, saytext, lang):

        appSecret = self.set['main_setting']['TTS']['youdao']['appkey']
        appKey = self.set['main_setting']['TTS']['youdao']['appid']
        data = {}
        salt = random.randint(1, 65536)

        sign = appKey + q + str(salt) + appSecret
        m1 = md5.new()
        m1.update(sign)
        sign = m1.hexdigest()

        data['appKey'] = appKey
        data['q'] = q
        data['salt'] = salt
        data['sign'] = sign
        data['langType'] = lang
        response = requests.post('http://openapi.youdao.com/ttsapi',
                                 data=data)

        contentType = response.headers['content-type']
        
        if contentType == "audio/mp3":
            filePath = "/home/pi/xiaolan/memory_center/musiclib/" + 'say' + ".mp3"
            fo = open(filePath,'wb')
            fo.write(response.content)
            fo.close()
            return {'States': 'YoudaoTTSComplete'}
        else:
            self.tts('对不起，我的语言中枢出错了，我不能跟你说话了', self.set['main_setting']['TTS']['youdao']['lang'])
            speaker.speak()
            return {'States': 'Error:YoudaoTTSError'}

