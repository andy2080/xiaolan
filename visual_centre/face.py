# -*- coding: utf-8 -*-
# 人脸唤醒

import os
import sys
import json
import requests
import cv2
import base64
sys.path.append('/home/pi/xiaolan/')
from speech_center.tts import baidu_tts
from speech_center.tts import youdao_tts
from speech_center.nlu import Nlu
from auditory_center.recorder import recorder
import setting
from network_center.xiaolanClientToServer import ClientToServer
sys.path.append('/home/pi/xiaolan/speech_center')
import speaker

def get_token():

    AK = setting.setting()['main_setting']['OCR']['baidu']['AK']
    SK = setting.setting()['main_setting']['OCR']['baidu']['SK']
    params = urllib.urlencode({'grant_type': 'client_credentials',
                               'client_id': AK,
                               'client_secret': SK})
    headers = {"Content-Type', 'application/json; charset=UTF-8"}
    r = requests.get('https://aip.baidubce.com/oauth/2.0/token?',
                     params=params,
                     headers=headers)
    token = r.json()['access_token']
    return token

def get_faceimage():

    os.system('raspistill -t 2000 -o /home/pi/xiaolan/memory_center/facedatebase/newface.jpg')
    return '/home/pi/xiaolan/memory_center/facedatebase/newface.jpg'

def awaken(self):

    r = recorder()
    if setting.setting()['main_setting']['TTS']['service'] == 'baidu':
            tts = baidu_tts()
            token = tts.get_token()
    elif setting.setting()['main_setting']['TTS']['service'] == 'youdao':
            tts = youdao_tts()
            token = setting.setting()['main_setting']['TTS']['youdao']['lang']
    if setting.setting()['main_setting']['STT']['service'] == 'baidu':
            stt = baidu_stt()
            token = stt.get_token()
    elif setting.setting()['main_setting']['STT']['service'] == 'ifly':
            stt = ifly_stt()
            token = setting.setting()['main_setting']['STT']['ifly']['key']
    tok = get_token()
    faceimg = '/home/pi/xiaolan/memory_center/facedatebase/face.png'
    while 0 = 0:
        try:
            i = open(faceimg)
        except IOError:
            tts.tts('请对准摄像头，我们将采集你的头像', token)
            speaker.speak()
            os.system('raspistill -t 2000 -o /home/pi/xiaolan/memory_center/facedatebase/face.jpg')
        url = 'https://aip.baidubce.com/rest/2.0/face/v3/match'
        headers = {'Content-Type': 'application/json'}
        nowfaceimage = get_faceimage()
        body = [
            {
                "image": base64.b64encode(nowfaceimage),
                "image_type": "BASE64",
                "face_type": "LIVE"
            },
            {
                "image": base64.b64encode(self.faceimage),
                "image_type": "BASE64",
                "face_type": "LIVE"
            }
        ]
        r = requests.post(url,
                          headers=headers,
                          data=body)
        json = r.json()
        if json['score'] > 79:
            break
        else:
            pass
    tts.tts('请问有什么需要吗？', token)
    speaker.speak()
    r = r.record()
    text = stt.stt('./voice.wav', tokens)
    xlnlu = Nlu()
    if text == None or text == '':
        speaker.speacilrecorder()
    else:
        intentdict = xlnlu.xl_intent(text)
        cts = ClientToServer()
        cts.ClientReq(intentdict['intent'], intentdict['slots'], intentdict)




