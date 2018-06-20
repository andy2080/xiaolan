# -*- coding: UTF-8 -*-
import sys
import requests
import os
import json
import demjson
import random
import httplib
import urllib
import urllib2
sys.path.append('/home/pi/xiaolan/')
import speaker
from stt import baidu_stt
from tts import baidu_tts
from tts import youdao_tts
from recorder import recorder
import setting

def start(tok):
    
    main(tok)

def lang_choose(text, tok):
    
    if '英语' in text or '英文' in text:
        lang = 'en'
    elif '法语' in text or '法文' in text:
        lang = 'fr'
    elif '中文' in text or '简体中文' in text:
        lang = 'zh-CHS'
    elif '俄语' in text or '俄文' in text:
        lang = 'ru'
    elif '韩语' in text or '韩文' in text:
        lang = 'ko'
    elif '日语' in text or '日文' in text:
        lang = 'ja'
    elif '葡萄牙文' in text or '葡萄牙语' in text:
        lang = 'pt'
    elif '西班牙文' in text or '西班牙语' in text:
        lang = 'es'
    elif '越南语' in text or '越南文' in text:
        lang = 'vi'
    else:
        lang = 'en'
    return lang
    
def main(tok):
    
    bt = baidu_tts()
    bs = baidu_stt(1, 2, 3, 4)
    r = recorder()
    youdao = youdao_tts()
    
    appKey = selfset['ts']['appkey']
    secretkey = selfset['ts']['secretkey']
    httpClient = None
    myurl = '/api'
    q = 'good'
    
    bt.tts('请问您要翻译的是什么语言？', tok)
    speaker.speak()
    speaker.ding()
    r.record()
    speaker.dong()
    fromLang = lang_choose(bs.stt('./voice.wav', tok), tok)
    bt.tts('请问您要翻译为什么语言？', tok)
    speaker.speak()
    speaker.ding()
    r.record()
    speaker.dong()
    toLang = lang_choose(bs.stt('./voice.wav', tok), tok)
    bt.tts('请说出您要翻译的内容', tok)
    speaker.speak()
    speaker.ding()
    r.tsrecord()
    speaker.dong()
    tstext = bs.stt('./voice.wav', tok)
    
    salt = random.randint(1, 65536)
    sign = appKey+q+str(salt)+secretKey
    m1 = md5.new()
    m1.update(sign)
    sign = m1.hexdigest()
    myurl = myurl + '?appKey=' + appKey + '&q=' + urllib.quote(q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(salt) + '&sign=' + sign
 
    try:
        httpClient = httplib.HTTPConnection('openapi.youdao.com')
        httpClient.request('GET', myurl)
 
        #response是HTTPResponse对象
        response = httpClient.getresponse()
        json = json.loads(response.read())
        try:
            youdao.tts('第一种意思为，' + json['translation'][0] + '，第二种意思为，' + json['translation'][1], toLang)
            speaker.speak()
        except:
            youdao.tts('翻译结果为' + json['translation'][0], toLang)
            speaker.speak()
    except Exception, e:
        print e
    finally:
        if httpClient:
            httpClient.close()
    
    
    
  
