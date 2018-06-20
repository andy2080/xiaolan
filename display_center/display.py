# -*- coding: utf-8 -*-

import os
import sys
import requests
import json
import demjson
sys.path.append('/home/pi/xiaolan/')
from speech_center.stt import baidu_stt
from speech_center.tts import baidu_tts
from speech_center.tts import youdao_tts
import speech_center.speaker

def dis(json, intentdict, tok):
    bt = baidu_tts()
    bs = baidu_stt(1, 2, 3, 4)
    if json['card'] == None or json['cord'] == '':
        bt.tts(json['outputSpeech'], tok)
        speaker.speak()
