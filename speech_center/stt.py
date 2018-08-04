# -*- coding: utf-8 -*-
# 百度STT

# description:
# author: xiaoland
# create_time: 2018/4/23

"""
    desc:pass
"""

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
import hmac
from hashlib import sha1
sys.path.append('/home/pi/xiaolan/')
from Base import xiaolanBase


domian = 'a'

class baidu_stt(xiaolanBase):

    def __init__(self):

        super(baidu_stt, self).__init__()

    def get_token(self): #获取token

        AK = self.set['main_setting']['STT']['baidu']['AK']
        SK = self.set['main_setting']['STT']['baidu']['SK']
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

    def stt_start(self, fp, token):
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
        lang = self.set['main_setting']['sys_lang']
        if lang == 'En':
            dev_id = 1737
        elif lang == 'Zh-Hans':
            dev_id = 1936
        elif lang == 'Zh-Yue':
            dev_id = 1637
        elif lang == 'Zh-Chun':
            dev_id = 1837
        else:
            dev_id = 1536
        dataf = {"format": "wav",
                "token": token,
                "len": len(audio),
                "rate": frame_rate,
                "speech": base_data,
                "dev_pid": dev_id,
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
                return {'States': 'BaiduSTTComplete', 'Text': text}
        except requests.exceptions.HTTPError:
            print ('Request failed with response: %r',
                   r.text)
            return {'States': 'BaiduSTTError:Request failed with response'}
        except requests.exceptions.RequestException:
            print ('Request failed.')
            return {'States': 'BaiduSTTError:Request failed.'}
        except ValueError as e:
            print ('Cannot parse response: %s',
                                  e.args[0])
            return {'States': 'BaiduSTTError:Request failed.'}
        except KeyError:
            print ('Cannot parse response')
            return {'States': 'BaiduSTTError:Cannot parse response'}
        else:
            transcribed = []
            if text:
                transcribed.append(text.upper())
            print (json)

    def stt_starts(self, fn, token):

        """
        百度实时语音识别
        :param fn: 文件路径
        :param token: token
        :return:
        """
        time.sleep(1)
        texts = []
        lang = self.set['main_setting']['sys_lang']
        if lang == 'En':
            dev_id = 1737
        elif lang == 'Zh-Hans':
            dev_id = 1936
        elif lang == 'Zh-Yue':
            dev_id = 1637
        elif lang == 'Zh-Chun':
            dev_id = 1837
        else:
            dev_id = 1536

        f = open(fn, 'rb')
        file_content = len(f.read())
        a = 0
        for long in file_content:
            if long % 30720 == 0:
                times = 1
                timess = int(long) / 30720
                while 1 == 1:

                    if times == timess + 1:
                        info = {'States': 'BaiduSttComplete', 'Text': texts}
                        break
                    else:
                        file = f.read()
                        file = file[a:times * 30720]
                        base_data = base64.b64encode(file)

                        dataf = {"format": "wav",
                                 "token": token,
                                 "rate": 16000,
                                 "speech": base_data,
                                 "dev_pid": dev_id,
                                 "cuid": 'b0-10-41-92-84-4d',
                                 "channel": 1}

                        data = demjson.encode(dataf)

                        r = requests.post('http://vop.baidu.com/server_api',
                                          data=data,
                                          headers={'content-type': 'application/json'})

                        try:
                            if 'result' in r.json():
                                text = r.json()['result'][0].encode('utf-8')
                                if text == None:
                                    texts.append('')
                                else:
                                    texts.append(text)
                                if a == 0:
                                    a = 30720
                                else:
                                    a = times * 30720
                                times += 1
                            else:
                                info = {'States': 'Error:ResultUnfound', 'Text': None}
                                break
                        except requests.exceptions.HTTPError:
                            print ('Request failed with response: %r',
                                   r.text)
                            info = {'States': 'BaiduSTTError:Request failed with response', 'Text': None}
                            break
                        except requests.exceptions.RequestException:
                            print ('Request failed.')
                            info = {'States': 'BaiduSTTError:Request failed.', 'Text': None}
                            break
                        except KeyError:
                            print ('Cannot parse response')
                            info = {'States': 'BaiduSTTError:Cannot parse response', 'Text': None}
                            break
                break
            else:
                times = 1
                timess = long / 30720 - long // 30720
                while 1 == 1:

                    if times == timess + 1:
                        file = f.read()
                        file = file[a:times * 30720]
                        base_data = base64.b64encode(file)

                        dataf = {"format": "wav",
                                 "token": token,
                                 "rate": 16000,
                                 "speech": base_data,
                                 "dev_pid": dev_id,
                                 "cuid": 'b0-10-41-92-84-4d',
                                 "channel": 1}

                        data = demjson.encode(dataf)

                        r = requests.post('http://vop.baidu.com/server_api',
                                          data=data,
                                          headers={'content-type': 'application/json'})

                        try:
                            if 'result' in r.json():
                                text = r.json()['result'][0].encode('utf-8')
                                if text == None:
                                    texts.append('')
                                else:
                                    texts.append(text)
                                if a == 0:
                                    a = 30720
                                else:
                                    a = times * 30720
                                times += 1

                            else:
                                info = {'States': 'Error:ResultUnfound', 'Text': None}
                                break
                        except requests.exceptions.HTTPError:
                            print ('Request failed with response: %r',
                                   r.text)
                            info = {'States': 'BaiduSTTError:Request failed with response', 'Text': None}
                            break
                        except requests.exceptions.RequestException:
                            print ('Request failed.')
                            info = {'States': 'BaiduSTTError:Request failed.', 'Text': None}
                            break
                        except KeyError:
                            print ('Cannot parse response')
                            info = {'States': 'BaiduSTTError:Cannot parse response', 'Text': None}
                            break
                        info = {'States': 'BaiduSttComplete', 'Text': texts}
                        break
                    else:
                        file = f.read()
                        file = file[a:times * 30720]
                        base_data = base64.b64encode(file)

                        dataf = {"format": "wav",
                                 "token": token,
                                 "rate": 16000,
                                 "speech": base_data,
                                 "dev_pid": dev_id,
                                 "cuid": 'b0-10-41-92-84-4d',
                                 "channel": 1}

                        data = demjson.encode(dataf)

                        r = requests.post('http://vop.baidu.com/server_api',
                                          data=data,
                                          headers={'content-type': 'application/json'})

                        try:
                            if 'result' in r.json():
                                text = r.json()['result'][0].encode('utf-8')
                                if not text:
                                    texts.append('')
                                else:
                                    texts.append(text)
                                if a == 0:
                                    a = 30720
                                else:
                                    a = times * 30720
                                times += 1
                            else:
                                info = {'States': 'Error:ResultUnfound', 'Text': None}
                                break
                        except requests.exceptions.HTTPError:
                            print ('Request failed with response: %r',
                                   r.text)
                            info = {'States': 'BaiduSTTError:Request failed with response', 'Text': None}
                            break
                        except requests.exceptions.RequestException:
                            print ('Request failed.')
                            info = {'States': 'BaiduSTTError:Request failed.', 'Text': None}
                            break
                        except KeyError:
                            print ('Cannot parse response')
                            info = {'States': 'BaiduSTTError:Cannot parse response', 'Text': None}
                            break
                break
        f.close()
        return info

class ifly_stt(xiaolanBase):

    def __init__(self):

        super(ifly_stt, self).__init__()

    def stt_start(self, fn, tok):

        f = open(fn, 'rb')
        file_content = f.read()
        base64_audio = base64.b64encode(file_content)
        body = urllib.urlencode({'audio': base64_audio})

        api_key = self.set['main_setting']['STT']['ifly']['key']
        param = {"engine_type": "sms16k", "aue": "raw"}

        x_appid = self.set['main_setting']['STT']['IFLY']['appid']
        x_param = base64.b64encode(json.dumps(param).replace(' ', ''))
        x_header = {'X-Appid': x_appid,
                    'X-CurTime': int(int(round(time.time() * 1000)) / 1000),
                    'X-Param': x_param,
                    'X-CheckSum': hashlib.md5(api_key + str(x_time) + x_param).hexdigest()
                    }
        req = urllib2.Request('http://api.xfyun.cn/v1/service/v1/iat', body, x_header)
        result = urllib2.urlopen(req)
        result = result.read()
        return {'States': 'IflySTTComplete', 'Text': json.loads(result)['data']}

    def stt_starts(self, fn, tok):

        """
        讯飞实时语音识别
        :param fn: 文件路径
        :param tok: 其他
        :return:
        """
        sleep(1)
        texts = []
        f = open(fn, 'rb')
        file_content = len(f.read())
        for long in file_content:
            times = 1
            timess = long / 30720
            a = 0
            if long % 30720 == 0:
                while 1 == 1:
                    if times == timess:
                        info = {'States': 'BaiduSttComplete', 'Text': texts}
                        break
                    else:
                        file = f.read()
                        file = file[a:times * 30720]
                        base64_audio = base64.b64encode(file)
                        body = urllib.urlencode({'audio': base64_audio})

                        api_key = self.set['main_setting']['STT']['ifly']['key']
                        param = {"engine_type": "sms16k", "aue": "raw"}

                        x_appid = self.set['main_setting']['STT']['IFLY']['appid']
                        x_param = base64.b64encode(json.dumps(param).replace(' ', ''))
                        x_header = {'X-Appid': x_appid,
                                    'X-CurTime': int(int(round(time.time() * 1000)) / 1000),
                                    'X-Param': x_param,
                                    'X-CheckSum': hashlib.md5(api_key + str(x_time) + x_param).hexdigest()
                                    }
                        req = urllib2.Request('http://api.xfyun.cn/v1/service/v1/iat', body, x_header)
                        result = urllib2.urlopen(req)
                        result = result.read()
                        a = times * 30720
                        times += 1
                        info = {'States': 'IflySTTComplete', 'Text': texts.append(json.loads(result)['data'])}

        f.close()
        return info

class 	TencentStt(xiaolanBase):

    def __init__(self):

        super(TencentStt, self).__init__()

    def get_auth_signature(self, req):

        """
        获取腾讯云请求签名认证
        :return:
        """
        SK = self.set['main_setting']['STT']['tencent']['SK']
        signf = 'POSTaai.tencentcloudapi.com/?' + req
        signs = hmac.new(signf, SK, sha1).digest()
        signt = base64.b64encode(signs)
        return urllib.parse.quote(signt)


    def stt_starts(self, fn, token):

        """
        腾讯云实时语音识别
        :param fn: 文件路径
        :param token: 其他
        :return:
        """
        time.sleep(1)
        texts = []
        url = 'https://aai.tencentcloudapi.com/?'
        SI = self.set['main_setting']['STT']['tencent']['SI']

        time = 1

        while 1 == 1:
            if time == 6:
                break
            else:
                f = open(fn, 'rb')
                voice = f.read()
                audio = base64.b64encode(voice)
                data = {
                    'Action': 'SentenceRecognition',
                    'Data': audio,
                    'DataLen': long,
                    'EngSerViceType': '16k',
                    'Nonce': 12345,
                    'ProjectId': 0,
                    'SubServiceType': 1,
                    'SourceType': 1,
                    'SecretId': SI,
                    'Timestamp': time.time(),
                    'UsrAudioKey': 'xiaolan',
                    'Version': '2018-05-22',
                    'VoiceFormat': 'wav'
                }
                signtrue = self.get_auth_signature(urllib.parse.urlencode(data))
                data['Signature'] = signtrue
                data = urllib.parse.urlencode(data)

                url = url + data
                r = requests.post(url)

                text = r.json()['Response']['Result']
                if not text or text == '':
                    texts.append('')
                else:
                    texts.append(text)
                time += 1




