# -*- coding: utf-8 -*-
''' 闹钟 '''
import json
import sys
import os
import requests
import datetime
import time
sys.path.append('/home/pi/xiaolan/')
from stt import baidu_stt
from tts import baidu_tts
import speaker
from recorder import recorder

def start(tok):
    
    main(tok)
  
def main(tok):
    bt = baidu_tts()
    bs = baidu_stt(1, 2, 3, 4)
    r.recorder()
    bt.tts('请问您要设定什么时候的闹钟？', tok)
    speaker.speak()
    bt.tts('支持下午几点的说法', tok)
    speaker.speak()
    speaker.ding()
    r.exrecord()
    speaker.dong()
    text = bs.stt('./voice.wav', tok).replace('，', '')
    if '重复闹钟' in text:
        if '下午' in text or '上午' in text:
            text = text.choose_date(text, text.rfind('重复闹钟'), tok)
            
        
    
