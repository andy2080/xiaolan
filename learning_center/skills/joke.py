# -*- coding: utf-8 -*-
''' 故事/笑话 '''
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
    
    url = 'http://api.avatardata.cn/Joke/QueryJokeByTime?key='
    selfset = setting.setting()
    key = selfset['joke']['key']
    bt = baidu_tts()
    
    r = requests.post(url + key + '&sort=asc&time=1418745237')
    
    json = r.json()
    
    bt.tts(json['result'][random.randint(0,9)]['content'], tok)
    speaker.speak()
