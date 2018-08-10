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
import threading
import random
from hashlib import sha1
sys.path.append('/home/pi/xiaolan/')
from Base import xiaolanBase


domian = 'a'

class BaiduStt(xiaolanBase):

    def __init__(self):

        super(BaiduStt, self).__init__()

    def get_token(self): #获取token

        token = ''
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

        """
        百度语音识别
        :param fp:文件
        :param token: token
        :return:
        """
        try:
            wav_file = open(fp, "rb")
        except IOError:
            self.log('write', {'log': 'Error:IoError:UnfoundFile', 'level': 'error'})
            return {'States': 'Error', 'Text': None}
        # 设置识别模型
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
        # 多线程处理判断
        if len(wav_file) < 10000:

            data = {"format": "wav",
                     "token": token,
                     "len": len(wav_file.read()),
                     "rate": 16000,
                     "speech": base64.b64encode(wav_file.read()),
                     "dev_pid": dev_id,
                     "cuid": 'b0-10-41-92-84-4d',
                     "channel": 1}

            data = demjson.encode(data)

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

        else:

            long = len(wav_file)
            thread_long = long / 6
            threads = []
            stt_thread_1 = threading.Thread(target=BaiduStt.stt_thread_1, args=(self, token, fn, 0, thread_long, dev_id))
            stt_thread_2 = threading.Thread(target=BaiduStt.stt_thread_2, args=(self, token, fn, thread_long, thread_long * 2, dev_id))
            stt_thread_3 = threading.Thread(target=BaiduStt.stt_thread_3, args=(self, token, fn, thread_long * 2, thread_long * 3, dev_id))
            stt_thread_4 = threading.Thread(target=BaiduStt.stt_thread_4, args=(self, token, fn, thread_long * 3, thread_long * 4, dev_id))
            stt_thread_5 = threading.Thread(target=BaiduStt.stt_thread_5, args=(self, token, fn, thread_long * 4, thread_long * 5, dev_id))
            stt_thread_6 = threading.Thread(target=BaiduStt.stt_thread_6, args=(self, token, fn, thread_long * 5, long, dev_id))
            threads.append(stt_thread_1)
            threads.append(stt_thread_2)
            threads.append(stt_thread_3)
            threads.append(stt_thread_4)
            threads.append(stt_thread_5)
            threads.append(stt_thread_6)
            stt_thread_1.start()
            stt_thread_2.start()
            stt_thread_3.start()
            stt_thread_4.start()
            stt_thread_5.start()
            stt_thread_6.start()
            for t in threads:
                t.join()
            f = open("/home/pi/xiaolan/memory_center/more/text_1.txt");text_1 = f.read();f.close()
            f = open("/home/pi/xiaolan/memory_center/more/text_2.txt");text_2 = f.read();f.close()
            f = open("/home/pi/xiaolan/memory_center/more/text_3.txt");text_3 = f.read();f.close()
            f = open("/home/pi/xiaolan/memory_center/more/text_4.txt");text_4 = f.read();f.close()
            f = open("/home/pi/xiaolan/memory_center/more/text_5.txt");text_5 = f.read();f.close()
            f = open("/home/pi/xiaolan/memory_center/more/text_6.txt");text_6 = f.read();f.close()
            text = text_1 + text_2 + text_3 + text_4 + text_5 + text_6
            return {'States': 'Complete', 'Text': text}

    def stt_thread_1(self, token, fn, start, end, dev_id):

        """
        STT识别线程1
        :param start: 开始
        :param end: 结束
        :param fn: 文件
        :param dev_id: 语言模型
        :param token: token
        :return:
        """
        f = open(fn, "rb")
        audio = base64.b64(f.read()[start:end])
        data = {
                 "format": "wav",
                 "token": token,
                 "len": len(f.read()[start:end]),
                 "rate": 16000,
                 "speech": audio,
                 "dev_pid": dev_id,
                 "cuid": 'b0-10-41-92-84-4d',
                 "channel": 1
        }

        data = demjson.encode(data)

        r = requests.post('http://vop.baidu.com/server_api',
                          data=data,
                          headers={'content-type': 'application/json'})

        try:
            r.raise_for_status()
            text = ''
            if 'result' in r.json():
                text = r.json()['result'][0].encode('utf-8')
                f = open("/home/pi/xiaolan/memory_center/more/text_1.txt", "w")
                f.write(text)
                f.close()
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
            print(json)

    def stt_thread_2(self, token, fn, start, end, dev_id):

        """
        STT识别线程2
        :param start: 开始
        :param end: 结束
        :param fn: 文件
        :param dev_id: 语言模型
        :param token: token
        :return:
        """
        f = open(fn, "rb")
        audio = base64.b64(f.read()[start:end])
        data = {
                 "format": "wav",
                 "token": token,
                 "len": len(f.read()[start:end]),
                 "rate": 16000,
                 "speech": audio,
                 "dev_pid": dev_id,
                 "cuid": 'b0-10-41-92-84-4d',
                 "channel": 1
        }

        data = demjson.encode(data)

        r = requests.post('http://vop.baidu.com/server_api',
                          data=data,
                          headers={'content-type': 'application/json'})

        try:
            r.raise_for_status()
            text = ''
            if 'result' in r.json():
                text = r.json()['result'][0].encode('utf-8')
                f = open("/home/pi/xiaolan/memory_center/more/text_2.txt", "w")
                f.write(text)
                f.close()
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
            print(json)

    def stt_thread_3(self, token, fn, start, end, dev_id):

        """
        STT识别线程3
        :param start: 开始
        :param end: 结束
        :param fn: 文件
        :param dev_id: 语言模型
        :param token: token
        :return:
        """
        f = open(fn, "rb")
        audio = base64.b64(f.read()[start:end])
        data = {
                 "format": "wav",
                 "token": token,
                 "len": len(f.read()[start:end]),
                 "rate": 16000,
                 "speech": audio,
                 "dev_pid": dev_id,
                 "cuid": 'b0-10-41-92-84-4d',
                 "channel": 1
        }

        data = demjson.encode(data)

        r = requests.post('http://vop.baidu.com/server_api',
                          data=data,
                          headers={'content-type': 'application/json'})

        try:
            r.raise_for_status()
            text = ''
            if 'result' in r.json():
                text = r.json()['result'][0].encode('utf-8')
                f = open("/home/pi/xiaolan/memory_center/more/text_3.txt", "w")
                f.write(text)
                f.close()
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
            print(json)

    def stt_thread_4(self, token, fn, start, end, dev_id):

        """
        STT识别线程4
        :param start: 开始
        :param end: 结束
        :param fn: 文件
        :param dev_id: 语言模型
        :param token: token
        :return:
        """
        f = open(fn, "rb")
        audio = base64.b64(f.read()[start:end])
        data = {
                 "format": "wav",
                 "token": token,
                 "len": len(f.read()[start:end]),
                 "rate": 16000,
                 "speech": audio,
                 "dev_pid": dev_id,
                 "cuid": 'b0-10-41-92-84-4d',
                 "channel": 1
        }

        data = demjson.encode(data)

        r = requests.post('http://vop.baidu.com/server_api',
                          data=data,
                          headers={'content-type': 'application/json'})

        try:
            r.raise_for_status()
            text = ''
            if 'result' in r.json():
                text = r.json()['result'][0].encode('utf-8')
                f = open("/home/pi/xiaolan/memory_center/more/text_4.txt", "w")
                f.write(text)
                f.close()
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
            print(json)

    def stt_thread_5(self, token, fn, start, end, dev_id):

        """
        STT识别线程5
        :param start: 开始
        :param end: 结束
        :param fn: 文件
        :param dev_id: 语言模型
        :param token: token
        :return:
        """
        f = open(fn, "rb")
        audio = base64.b64(f.read()[start:end])
        data = {
                 "format": "wav",
                 "token": token,
                 "len": len(f.read()[start:end]),
                 "rate": 16000,
                 "speech": audio,
                 "dev_pid": dev_id,
                 "cuid": 'b0-10-41-92-84-4d',
                 "channel": 1
        }

        data = demjson.encode(data)

        r = requests.post('http://vop.baidu.com/server_api',
                          data=data,
                          headers={'content-type': 'application/json'})

        try:
            r.raise_for_status()
            text = ''
            if 'result' in r.json():
                text = r.json()['result'][0].encode('utf-8')
                f = open("/home/pi/xiaolan/memory_center/more/text_5.txt", "w")
                f.write(text)
                f.close()
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
            print(json)

    def stt_thread_6(self, token, fn, start, end, dev_id):

        """
        STT识别线程6
        :param start: 开始
        :param end: 结束
        :param fn: 文件
        :param dev_id: 语言模型
        :param token: token
        :return:
        """
        f = open(fn, "rb")
        speech = base64.b64(f.read()[start:end])
        data = {
                 "format": "wav",
                 "token": token,
                 "len": len(f.read()[start:end]),
                 "rate": 16000,
                 "speech": audio,
                 "dev_pid": dev_id,
                 "cuid": 'b0-10-41-92-84-4d',
                 "channel": 1
        }

        data = demjson.encode(data)

        r = requests.post('http://vop.baidu.com/server_api',
                          data=data,
                          headers={'content-type': 'application/json'})

        try:
            r.raise_for_status()
            text = ''
            if 'result' in r.json():
                text = r.json()['result'][0].encode('utf-8')
                f = open("/home/pi/xiaolan/memory_center/more/text_6.txt", "w")
                f.write(text)
                f.close()
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
            print(json)

    def stt_starts(self, fp, token):

        """
        百度语音识别
        :param fp:文件
        :param token: token
        :return:
        """
        try:
            wav_file = wave.open(fp, 'rb')
        except IOError:
            self.log('write', {'log': 'Error:IoError:UnfoundFile', 'level': 'error'})
            return {'States': 'Error', 'Text': None}
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
        data = {"format": "wav",
                 "token": token,
                 "len": len(f.read()[start:end]),
                 "rate": frame_rate,
                 "speech": base_data,
                 "dev_pid": dev_id,
                 "cuid": 'b0-10-41-92-84-4d',
                 "channel": 1}

        data = demjson.encode(data)

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













class IflyStt(xiaolanBase):

    def __init__(self):

        super(IflyStt, self).__init__()

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



class 	TencentStt(xiaolanBase):

    def __init__(self):

        super(TencentStt, self).__init__()

    def urlencode(self, args):

        """
        进行字典排序和urlencode
        :return:
        """
        tuples = [(k, args[k]) for k in sorted(args.keys()) if args[k]]
        query_str = urllib.urlencode(tuples)
        return query_str

    def signify(self, args):

        """
        获取腾讯API签名认证
        :return:
        """
        app_key = self.set['main_setting']['STT']['tencent']['appkey']
        query_str = self.urlencode(args)
        query_str = query_str + '&app_key=' + app_key
        signiture = self.md5(query_str)
        return signiture


    def stt_start(self, fn, token):

        """
        腾讯AI开放平台实时语音识别
        :param fn: 文件路径
        :param token: token
        :return:
        """
        ext = 'wav'
        time.sleep(2)
        info = {}
        url = 'https://api.ai.qq.com/fcgi-bin/aai/aai_asrs'
        appid = self.set['main_setting']['STT']['tencent']['appid']

        wf = wave.open(fn)
        resp = {}
        total_len = wf.getnframes() * wf.getsampwidth()
        seq, end = 0, '0'
        while end != '1':
            data = wf.readframes(1024)
            length = len(data)
            end = '0' if length + seq < total_len else '1'

            args = {
                'app_id': appid,
                'time_stamp': str(int(time.time())),
                'nonce_str': '%.x' % random.randint(1048576, 104857600),
                'format': 2,
                'rate': 16000,
                'bits': 16,
                'seq': int(seq),
                'len': int(length),
                'end': end,
                'speech_id': '0',
                'speech_chunk': base64.b64encode(data),
                'cont_res': 0
            }

            signiture = self.signify(args)
            args['sign'] = signiture
            resp = requests.post(url,
                                 data=args)

            seq += length
        resp = json.loads(resp)
        try:
            info['Text'] = resp['data']['speech_text'].encode('utf-8')
        except KeyError:
            info['Text'] = None
            info['States'] = 'Error:KeyError:data_missing'
        else:
            info['States'] = 'Complete'
        return info




