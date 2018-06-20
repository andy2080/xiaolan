# -*- coding: utf-8 -*-

''' 地图技能 '''

import sys
import os
import urllib
import urllib2
import httplib
import requests
import json
import demjson
sys.path.append('/home/pi/xiaolan/')
import speaker
from recorder import recorder
from stt import baidu_stt
from tts import baidu_tts
import setting

def start(tok):
    
    m = map()
    m.main(tok)
    
class maps(object):
    
    def __init__(self):
      
        self.set = setting.setting()
    
    def ip_loc(self, tok):
        
        r = requests.ger('http://restapi.amap.com/v3/ip?' + 'output=json&key=' + self.set['maps']['key'])
        try:
            bt.tts('你在' + r.json()['province'] + r.json()['city'], tok)
            speaker.speak()
        except KeyError:
            bt.tts('位置获取失败', tok)
            speaker.speak()
    
    def near(self, place, tok):
        
        pass
        
    def go_way(self, place_f, place_s, tok):
        
        pass
    
    def main(self, tok):
        
        bt = baidu_tts()
        bs = baidu_stt(1, 2, 3, 4)
        r = recorder()
        m = maps()
        
        bt.tts('欢迎使用小蓝地图技能', tok)
        speaker.speak()
        bt.tts('支持查找路线，附近有什么服务等，如：从这里到美丽公园怎么走？，又比如：美丽公园附近有什么吃的？', tok)
        speaker.speak()
        bt.tts('请说出您的需要', tok)
        speaker.speak()
        speaker.ding()
        r.record()
        speaker.dong()
        text = bs.stt('./voice.wav', tok)
        command = m.choose_command(text, tok)
        
    def choose_command(self, text, tok):
        
        m = maps()
        bt = baidu_tts()
        bs = baidu_stt(1, 2, 3, 4)
        r = recorder()
        if '从' in text and '怎么去' in text:
            m.go_way(text[0:-7], text[-8:-4], tok)
        elif '我在哪' in text or '我的位置,' == text:
            m.ip_loc(tok)
        elif '从' in text and '怎么走' in text:
            m.go_way(text[0:-7], text[-8:-4], tok)
        elif '附近' in text:
            m.near(text[0:5], tok)
        else:
            bt.tts('对不起，暂时不支持该功能', tok)
            speaker.speak()
