# -*- coding: utf-8 -*-
''' 新闻 '''
import json
import sys
import os
import requests
import time
import random
sys.path.append('/home/pi/xiaolan/')
from stt import baidu_stt
from tts import baidu_tts
from recorder import recorder
import speaker
import setting

def start(tok):
    
    main(tok)
    
def main(tok):
    setting = selfset.setting()
    APPKEY = selfset['news']['key']
    url = 'http://v.juhe.cn/toutiao/index?type='
    r = recorder()
    bt = baidu_tts()
    bs = baidu_stt(1, 'a', 2, '{')
    
    bt.tts('请问您要听什么新闻?', tok)
    speaker.speak()
    speaker.ding()
    r.record()
    speaker.dong()
    text = bs.stt('./voice.wav', tok)
    
    if '国内新闻' in text:
        r = requests.post(url + 'guonei' + '&key=' + APPKEY)
        json = r.json()
        bt.tts(json['result']['data'][random.randint(0,9)]['title'], tok)
        speaker.speak()
    elif '国际新闻' in text:
        r = requests.post(url + 'guoji' + '&key=' + APPKEY)
        json = r.json()
        saytext = json['result']['data'][random.randint(0,9)]['title']
        bt.tts(saytext, tok)
        speaker.speak()
    elif '科技新闻' in text:
        r = requests.post(url + 'keji' + '&key=' + APPKEY)
        json = r.json()
        bt.tts(json['result'][random.randint(0,9)]['title'], tok)
        speaker.speak()
    elif '体育新闻' in text:
        r = requests.post(url + 'tiyu' + '&key=' + APPKEY)
        json = r.json()
        bt.tts(json['result'][random.randint(0,9)]['title'], tok)
        speaker.speak()
    else:
        r = requests.post(url + 'top' + '&key=' + APPKEY)
        json = r.json()
        bt.tts(json['result'][random.randint(0,9)]['title'], tok)
        speaker.speak()
    
