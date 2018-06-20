# -*- coding: utf-8 -*-

import sys
import os
import pygame
import requests
import RPi.GPIO as gpio
import json
import time
sys.path.append('/home/pi/xiaolan/')
import speaker
from stt import baidu_stt
from tts import baidu_tts
from recorder import recorder

__author__ = 'Caibiy'

import Adafruit_DHT,os,time,datetime,sqlite3,uuid
conn,cursor=(None,None)
#gpio
@unique

def start(tok):
  
	gpioc = gpioc()
	gpioc.main(tok)


class gpioc(object):

        def __init__(self):
                
                pass
        def choose_gpio(self, text, tok):

                if '一' in text:
                        gpio_n = 1
                elif '二' in text:
                        gpio_n = 2
                elif '三' in text:
                        gpio_n = 3
                elif '四' in text:
                        gpio_n = 4
                elif '五' in text:
                        gpio_n = 5
                elif '六' in text:
                        gpio_n = 6
                elif '七' in text:
                        gpio_n = 7
                elif '八' in text:
                        gpio_n = 8
                elif '九' in text:
                        gpio_n = 9
                elif '十' in text:
                        gpio_n = 10
                elif '十一' in text or '11' in text:
                        gpio_n = 11
                elif '十二' in text or '12' in text:
                        gpio_n = 12
                elif '十三' in text or '13' in text:
                        gpio_n = 13
                elif '十四' in text or '14' in text:
                        gpio_n = 14
                elif '十五' in text or '15' in text:
                        gpio_n = 15
                elif '十六' in text or '16' in text:
                        gpio_n = 16
                elif '十七' in text or '17' in text:
                        gpio_n = 17
                elif '十八' in text or '18' in text:
                        gpio_n = 18
                elif '十九' in text or '19' in text:
                        gpio_n = 19
                elif '二十' in text or '20' in text:
                        gpio_n = 20
                elif '二十一' in text or '21' in text:
                        gpio_n = 21
                elif '二十二' in text or '22' in text:
                        gpio_n = 22
                elif '二十三' in text or '23' in text:
                        gpio_n = 23
                elif '二十四' in text or '24' in text:
                        gpio_n = 24
                elif '二十五' in text or '25' in text:
                        gpio_n = 25
                elif '二十六' in text or '26' in text:
                        gpio_n = 26
                elif '二十七' in text or '27' in text:
                        gpio_n = 27
                elif '二十八' in text or '28' in text:
                        gpio_n = 28
                elif '二十九' in text or '29' in text:
                        gpio_n = 29
                elif '三十' in text or '30' in text:
                        gpio_n = 30
                elif '三十一' in text or '31' in text:
                        gpio_n = 31
                elif '三十二' in text or '32' in text:
                        gpio_n = 32
                elif '三十三' in text or '33' in text:
                        gpio_n = 33
                elif '三十四' in text or '34' in text:
                        gpio_n = 34
                elif '三十五' in text or '35' in text:
                        gpio_n = 35
                elif '三十六' in text or '36' in text:
                        gpio_n = 36
                elif '三十七' in text or '37' in text:
                        gpio_n = 37
                elif '三十八' in text or '38' in text:
                        gpio_n = 38
                elif '三十九' in text or '39' in text:
                        gpio_n = 39
                elif '四十' in text or '40' in text:
                        gpio_n = 40
                else:
                        bt.tts('错误！超过针脚范围，warring', tok)
                        speaker.speak()
                        gpio_n = 'none'
                return gpio_n

        def choose_mode(self, text, tok):

                if '打开' in text or '启动' in text:
                        mode = 1
                elif '关闭' in text or '低电平' in text:
                        mode = 0
                elif '高电平' in text:
                        mode = 1
                else:
                        mode = 'none'
                        bt.tts('对不起，暂时不支持该操作', tok)
                        speaker.speak()
                return mode
                
        def main(self, tok):

                bt = baidu_tts()
                bs = baidu_stt(1, 2, 3, 4)
                r = recorder()
                gpioc = gpioc()

                bt.tts('请说出要控制的针脚和控制模式，如打开针脚十七', tok)
                speaker.speak()
                speaker.ding()
                r.record()
                speaker.dong()
                text = bs.stt('./voice.wav', tok)
                while text == None or text == '':
                        bt.tts('对不起，我没有听清楚您说了什么，请说出要控制的针脚和控制模式，如打开针脚十七', tok)
                        speaker.speak()
                        speaker.speak()
                        speaker.ding()
                        r.record()
                        speaker.dong()
                        text = bs.stt('./voice.wav', tok)
                        if text != None or text!= '':
                                break
                else:
                        pass
                gpio_n = gpioc.choose_gpio(text, tok)
                gpio_m = gpioc.choose_mode(text, tok)
                if gpio_n == 'none':
                        os.system('python /home/pi/xiaolan/xldo.py awaken')
                else:
                        if gpio_m == 'none':
                                os.system('python /home/pi/xiaolan/xldo.py awaken')
                        else:
                                gpio.output(gpio_n, gpio_m)

                






                

#初始化数据库
def initDb():
	global conn,cursor
	conn = sqlite3.connect("./db/smarthome.db")
	cursor = conn.cursor()
	#图片表
	cursor.execute('''CREATE TABLE IF NOT EXISTS pic (
	 		picid  INT UNSIGNED  PRIMARY KEY ,
	 		time  VARCHAR (100) NOT NULL
			)''')
	#温度表
	cursor.execute('''CREATE TABLE IF NOT EXISTS dth (
	 		dthid  INT UNSIGNED  PRIMARY KEY ,
	 		temp  VARCHAR (100) NOT NULL,
			humidity VARCHAR(100) NOT NULL
			)''')
	#mq2表
	cursor.execute('''CREATE TABLE IF NOT EXISTS mq2 (
	 		mq2id  INT UNSIGNED  PRIMARY KEY ,
	 		lpg  VARCHAR (100) NOT NULL,
			co VARCHAR(100) NOT NULL,
			smoke VARCHAR(100) NOT NULL
			)''')
	#操作记录表
	cursor.execute('''CREATE TABLE IF NOT EXISTS operalog (
	 		id  INT UNSIGNED  PRIMARY KEY ,
			time VARCHAR(100) NOT NULL,
			operaid VARCHAR(100) NOT NULL,
			type VARCHAR(100) NOT NULL
			)''')
	conn.commit()
#执行sql
def executeDb(sql):
	global conn,cursor
	cursor.execute(sql)
	conn.commit()	
#主控包含传感器、蜂鸣器
class sth(object):
	sensor = Adafruit_DHT.DHT11
	@property
	def sensor(self):
		return self.sensor
	def __init__(self):
		#初始化mode
		os.system('gpio -g mode %s out' % gpio.pdht11.value)
		os.system('gpio -g mode %s out' % gpio.pmq2.value)
		os.system('gpio -g mode %s out' % gpio.pbuzzer.value)
	#蜂鸣器
	def buzzer(self):
		os.system('gpio -g write %s 1' % gpio.pbuzzer.value)
		time.sleep(0.5)
		os.system('gpio -g write %s 0' % gpio.pbuzzer.value)
	#读取dth11温度
	def readDth(self):
                bt = baidu_tts()
                bs = baidu_stt(1, 'a', '{', 3)
		humidity,temperature = Adafruit_DHT.read_retry(self.sensor,gpio.pdht11.value)
		if humidity is not None and temperature is not None:
			saytext = '湿度是,' + humidity + '温度是' + temperature
                tok = bt.get_token()
                bt.tts(saytext, tok)
                speaker.speak()
      
    
