# -*- coding: utf-8 -*-
'''图灵'''
import sys
import os
import requests
import json
import urllib2
import demjson
sys.path.append('/home/pi/xiaolan/')
from stt import baidu_stt
from tts import baidu_tts
import speaker
from recorder import recorder
import setting

def start(text, tok):
  
    main(text, tok)
    
def main(text, tok):
    
    selfset = setting.setting()
    ak = selfset['tuling']['key']
    ui = selfset['tuling']['user_id']
    url = 'http://openapi.tuling123.com/openapi/api/v2'
    data = {
	      "reqType":0,
              "perception": {
                  "inputText": {
                      "text": text
                  },
              },
              "userInfo": {
                  "apiKey": ak,
                  "userId": ui
              }
           }
    talkback = requests.post(url, data=json.dumps(data))
    bt = baidu_tts()
    bt.tts(talkback.json()["results"][-1]["values"]["text"].encode('utf-8','strict'), tok)
    speaker.speak()
    
