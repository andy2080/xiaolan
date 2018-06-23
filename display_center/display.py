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
from speech_center.stt import ifly_stt
import speech_center.speaker

class ScreenDisplay(object):
    
    def __init__(self):
        pass
    def CardDo(self, info):
        pass
