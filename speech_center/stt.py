# -*- coding: utf-8 -*-
# 百度STT
import sys
import requests
import os
import json
import wave
import pyaudio
import time
import os.path
import demjson
import base64
import urllib
import urllib2
sys.path.append('/home/pi/xiaolan/')
import setting


domian = 'a'

class baidu_stt(object):
    def __init__(self, text, token, domain, transcribed):
        self.text = text
        self.domian = json
        self.token = token
        self.transcribed = transcribed

    def get_token(self): #获取token
        
        selfset = setting.setting()
        AK = selfset['main_setting']['STT']['baidu']['AK']
        SK = selfset['main_setting']['STT']['baidu']['SK']
        url = 'http://openapi.baidu.com/oauth/2.0/token'
        params = urllib.urlencode({'grant_type': 'client_credentials',
                                   'client_id': AK,
                                   'client_secret': SK})
        r = requests.get(url, params=params)
        try:
            r.raise_for_status()
            token = r.json()['access_token']
            return token
        except requests.exceptions.HTTPError:
            self._logger.critical('Token request failed with response: %r',
                                  r.text,
                                  exc_info=True)
            return token
        
    def stt(self, fp, token): #开始
        try:
            wav_file = wave.open(fp, 'rb')
        except IOError:
            self._logger.critical('wav file not found: %s',
                                  fp,
                                  exc_info=True)
            return []
        n_frames = wav_file.getnframes()
        frame_rate = wav_file.getframerate()
        audio = wav_file.readframes(n_frames)
        base_data = base64.b64encode(audio)
        if self.token == '':
            self.token = self.get_token()
        dataf = {"format": "wav",
                "token": token,
                "len": len(audio),
                "rate": frame_rate,
                "speech": base_data,
                "cuid": 'b0-10-41-92-84-4d',
                "channel": 1}
        
        data = demjson.encode(dataf)
        
        r = requests.post('http://vop.baidu.com/server_api',
                          data=data,
                          headers={'content-type': 'application/json'})
        
        try:
            r.raise_for_status()
            text = ''
            if 'result' in r.json():
                text = r.json()['result'][0].encode('utf-8')
                return text
        except requests.exceptions.HTTPError:
            print ('Request failed with response: %r',
                   r.text)
            return []
        except requests.exceptions.RequestException:
            print ('Request failed.')
            return []
        except ValueError as e:
            print ('Cannot parse response: %s',
                                  e.args[0])
            return []
        except KeyError:
            print ('Cannot parse response')
            return []
        else:
            transcribed = []
            if text:
                transcribed.append(text.upper())
            print (json)

class ifly_stt(object):
    def __init__(self):
        pass
    def stt(self, fn, tok):
        f = open(fn, 'rb')
        file_content = f.read()
        base64_audio = base64.b64encode(file_content)
        body = urllib.urlencode({'audio': base64_audio})

        api_key = setting.setting['main_setting']['STT']['ifly']['key']
        param = {"engine_type": "sms16k", "aue": "raw"}

        x_appid = setting.setting['main_setting']['STT']['IFLY']['appid']
        x_param = base64.b64encode(json.dumps(param).replace(' ', ''))
        x_header = {'X-Appid': x_appid,
                    'X-CurTime': int(int(round(time.time() * 1000)) / 1000),
                    'X-Param': x_param,
                    'X-CheckSum': hashlib.md5(api_key + str(x_time) + x_param).hexdigest()}
        req = urllib2.Request('http://api.xfyun.cn/v1/service/v1/iat', body, x_header)
        result = urllib2.urlopen(req)
        result = result.read()
        return json.loads(result)['data']
