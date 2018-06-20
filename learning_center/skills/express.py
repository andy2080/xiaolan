# coding=utf-8
'''快递查询技能'''

import sys
import os
import requests
import json
import demjson
import base64
import hashlib
import httplib
import urllib
import urllib2
import re
sys.path.append('/home/pi/xiaolan/')
import speaker
from tts import baidu_tts
from tts import youdao_tts
from stt import baidu_stt
from recorder import recorder
import setting

def start(tok):

    main(tok)
    
def number_choose(text, tok):
    
    bt = baidu_tts()
    try:
        text.replace('零', 0)
        text.replace('一', 1)
        text.replace('二', 2)
        text.replace('三', 3)
        text.replace('四', 4)
        text.replace('五', 5)
        text.replace('六', 6)
        text.replace('七', 7)
        text.replace('八', 8)
        text.replace('九', 9)
    except TypeError:
        return text
    except KeyError:
        return text
    else:
        return text
        
        
        
def main(tok):
    
    bt = baidu_tts()
    yt = youdao_tts()
    bs = baidu_stt(1, 2, 3, 4)
    r = recorder()
    
    selfset = setting.setting()
    hash = hashlib.md5()
    
    bt.tts('您好，请说出您要查询的快递单号', tok)
    speaker.speak()
    speaker.ding()
    r.exrecord()
    speaker.dong()
    
    requestData = {
                   'OrderCode': number_choose(bs.stt('./voice.wav', tok), tok),
                   'ShipperCode':'YTO',
                   'LogisticCode':'12345678'
                  }
    
    data = {
            'EBusinessID': selfset['express']['EBusinessID'],
            'RequestType': '1002',
            'RequestData': urllib.urlencode(str(requestData)) ,
            'DataType': '2',
           }
    hash.update(str(requestData) + selfset['express']['key'], encoding='utf-8')
    data['DataSign'] = urllib.urlencode(base64.b64encode(hash.hexdigest()))
    json = requests.post('http://api.kdniao.cc/Ebusiness/EbusinessOrderHandle.aspx',
                         data=data,
                         headers='application/x-www-form-urlencoded;charset=utf-8')
    try:
        bt.tts(json['Traces'][-1]['AcceptStation'], tok)
        speaker.speak()
    except KeyError:
        bt.tts('对不起，包裹信息查询失败', tok)
        speaker.speak()
        
        
    
    
    
    
    
    
