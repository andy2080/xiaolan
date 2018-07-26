# -*- coding: utf-8 -*-
# 人脸唤醒

import os
import sys
import json
import requests
import base64
sys.path.append('/home/pi/xiaolan/')
from Base import xiaolanBase
sys.path.append('/home/pi/xiaolan/speech_center')
import speaker

class XiaolanFaceAwaken(xiaolanBase):

    def __init__(self):

        super(XiaolanFaceAwaken, self).__init__()

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

        faceimg = '/home/pi/xiaolan/memory_center/facedatebase/face.png'
        while 0 == 0:
            try:
                i = open(faceimg)
            except IOError:
                self.tts.tts('请对准摄像头，我们将采集你的头像', self.tok)
                speaker.speak()
                os.system('raspistill -t 2000 -o /home/pi/xiaolan/memory_center/facedatebase/face.jpg')

            url = 'https://aip.baidubce.com/rest/2.0/face/v3/match?access_token=' + self.get_token()
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
        self.tts.tts(self.set['main_setting']['your_name'] + '请问有什么需要吗？', token)
        speaker.speak()
        r = r.record()
        text = self.stt.stt('./voice.wav', tokens)
        if text == None or text == '':
            speaker.speacilrecorder()
        else:
            intentdict = self.ClientToServer.XiaolanNluReq(text)
            self.ClientToServer.ClientSkillReq(intentdict['intent'], intentdict['slots'], intentdict)




