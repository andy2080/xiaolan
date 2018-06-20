# -*- coding: utf-8 -*-
'''天气'''
import sys
import os
import json
import requests
import urllib2
sys.path.append('/home/pi/xiaolan/')
from stt import baidu_stt
from tts import baidu_tts
import speaker
from recorder import recorder
import setting

def start(tok):

    main(tok)

def main(tok):

    bt = baidu_tts()
    bs = baidu_stt(1, 'a', 2, '{')
    r = recorder()
    selfset = setting.setting()
    host = 'https://api.seniverse.com/v3/weather/now.json?key='
    key = selfset['weather']['key']
    
    r = requests.get(host + key + '&location=ip&language=zh-Hans&unit=c')
    
    json = r.json()
    bt.tts(',今天的天气是,' + json['results'][0]['now']['text'] + '，温度是,'  + json['results'][0]['now']['temperature'] + '，摄氏度，', tok)
    speaker.speak()
