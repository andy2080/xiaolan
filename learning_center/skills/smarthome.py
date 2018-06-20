# -*- coding: UTF-8 -*-

import sys
import os
import requests
import json
import demjson
import time
sys.path.append('/home/pi/xiaolan/')
import speaker
from stt import baidu_stt
from tts import baidu_tts
from recorder import recorder
import setting

def start(tok):

    hass = hass()
    hass.main(tok)

class hass(object):

    def __init__(self):

        pass

    def main(self, tok):

        bt = baidu_tts()
        bs = baidu_stt(1, 2, 3, 4)
        r = recorder()
        h = hass()

        bt.tts('欢迎使用小蓝专用智能家居控制系统！请在，滴，一声之后说出指令，目前仅支持homeassistant', tok)
        speaker.speak()
        speaker.ding()
        r.record()
        speaker.dong()
        commands = bs.stt('./voice.wav', tok)
        while commands == None:
			sorry = '对不起，我没有听清楚，请重复一遍'
			bt.tts(sorry, tok)
			speaker.speak()
			speaker.ding()
			r.record()
			speaker.speak()
			commands = bs.stt('./voice.wav', tok)
			if commands != None:
				break
	else:
            pass
	#print commands[6:-2]
        hass.choose_command(commands)
        
    def choose_command(text):
	h = hass()
        if '打开' in text or '开启' in text:
            
            h.cortol('turn_on', text[text.rfind('打开') + 6:-1], tok)

        elif '关闭' in text or '关掉' in text:

            h.cortol('turn_off', text[text.rfind('关闭') + 6:-1], tok)
        
        elif '获取' in text:

            if '传感器' in command:
                getstatemode = 'sensor'
            else:
                getstatemode = 'switch'
            h.sensor(getstatemode, text[6:-2], tok)
	elif '怎么样' in text:
	    if '传感器' in command:
                getstatemode = 'sensor'
            else:
                getstatemode = 'switch'
            print text[9:-3]
            h.sensor(getstatemode, text[9:-3], tok)

    def e_id(self, tok):

        bt = baidu_tts()
	selfset = setting.setting()
	service = '/api/states'
	headers = {'x-ha-access': selfset['smarthome']['passwd'],
          	   'content-type': 'application/json'}
		
	r = requests.get(selfset['smarthome']['url'] + ':' + selfset['smarthome']['port'] + service,
			 headers=headers)
		
	r_json = r.json()
	e_id = {}
	try:
            for r_jsons in r_json:
                entity_id = r_jsons['entity_id']
                friendly_name = r_jsons['attributes']['friendly_name']
                domain = entity_id.split(".")[0]
                e_id[friendly_name] = entity_id
        except TypeError:
            bt.tts('homeassistant设备实体码获取失败', tok)
            speaker.speak()
	else:
	    return e_id


    def choose_color(self, text):

        if '红色' in text:
		c = 'red'
		return c
	elif '黄色' in text:
		c = 'yellow'
		return c
	elif '橙色' in text:
		c = 'orange'
		return c
	elif '绿色' in text:
		c = 'green'
		return c
	elif '蓝色' in text:
		c = 'blue'
		return c
	elif '紫色' in text:
		c = 'purple'
		return c
	elif '白色' in text:
		c = 'white'
		return c
	else:
		c = 'none'
		return c

    def cortol(self, cortolmode, cortolthings, tok):

        bt = baidu_tts()
        bs = baidu_stt(1, 2, 3, 4)
        r = recorder()
        h = hass()
        
        selfset = setting.setting()
	service = '/api/states'
	headers = {'x-ha-access': selfset['smarthome']['passwd'],
          	   'content-type': 'application/json'}

	try:
            en_id = h.e_id(tok)
            cortolthings = unicode(cortolthings, "utf-8", "ignore")

            if cortolmode == 'turn_on':
	    
                if en_id[cortolthings] != None:

                    if 'switch' in en_id[cortolthings]:

                        color_name = 'none'
                        service = '/api/services/switch/turn_on'

                    elif 'light' in en_id[cortolthings]:

                        bt.tts('请问要设置什么颜色，可以忽略', tok)
                        speaker.speak()
                        speaker.ding()
                        r.record()
                        speaker.dong()
                        text = bs.stt('./voice.wav', tok)
                        color_name = h.choose_color(text) 
                        service = '/api/services/light/turn_on'

            elif cortolmode == 'turn_off':

                if en_id[cortolthings] != None:

                    if 'switch' in en_id[cortolthings]:

                        color_name = 'none'
                        service = '/api/services/switch/turn_off'

                    elif 'light' in en_id[cortolthings]:

                        color_name = 'none'
                        service = '/api/services/light/turn_off'

            if color_name != 'none':

                dataf = {"color_name": color_name,
                         "entity_id": en_id[cortolthings].encode('utf-8')}
		data = json.dumps(dataf)
		
	    else:

                dataf = {"entity_id": en_id[cortolthings].encode('utf-8')}
		data = json.dumps(dataf)
                
        except KeyError:
			
		bt.tts('对不起，控制设备不存在，请注意！控制设备的名称得跟在homeassistant上设置的friendly，name一样', tok)
		speaker.speak()
	except TypeError:
		bt.tts('对不起，控制设备不存在，请注意！控制设备的名称得跟在homeassistant上设置的friendly，name一样', tok)
		speaker.speak()
	except ValueError:
		bt.tts('对不起，控制设备不存在，请注意！控制设备的名称得跟在homeassistant上设置的friendly，name一样', tok)
		speaker.speak()
	else:

            #print data
            r = requests.post(selfset['smarthome']['url'] + ':' + selfset['smarthome']['port'] + services,
                              headers=headers,
                              data=data)
            if cortolback.status_code == 200 or cortolback.status_code == 201:
                bt.tts('执行成功', tok)
                speaker.speak()
            else:
                bt.tts('执行错误', tok)
                speaker.speak()


    def sensor(self, getstatemode, getstatethings, tok):

        bt = baidu_tts()
        bs = baidu_stt(1, 2, 3, 4)
        r = recorder()
        h = hass()
        
        selfset = setting.setting()
	service = '/api/states'
	headers = {'x-ha-access': selfset['smarthome']['passwd'],
          	   'content-type': 'application/json'}

        if passwd != None or passwd != '':
            en_id = h.e_id(tok)
            service = '/api/states' + en_id[getstatethings]
            r = requests.get(selfset['smarthome']['url'] + ':' + selfset['smarthome']['port'] + service,
                             headers=headers)
            if cortolback.status_code == 200 or cortolback.status_code == 201:
                json = r.json()
                if json['state'] == 'turn_on' and getstatemode == 'switch':
                    bt.tts(getstatethins + '为开启状态', tok)
                    speaker.speak()
                elif json['state'] == 'turn_on' and getstatemode == 'switch':
                    bt.tts(getstatethings + '为关闭状态', tok)
                    speaker.speak()
                elif json['state'] == 'turn_on' and getstatemode == 'sensor':
                    bt.tts(getstatethings + '为关闭状态', tok)
                    speaker.speak()
                elif json['state'].isdigit() == True:
                    bt.tts(getstatethings + '的数据是' + json['state'], tok)
                    speaker.speak()
                else:
                    bt.tts('对不起，暂时不支持读取改设备的状态', tok)
                    speaker.speak()
            else:
                bt.tts('执行错误', tok)
                speaker.speak()
        else:
            pass
