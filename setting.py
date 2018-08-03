# -*- coding: utf-8 -*-
# 小蓝设置部分




def setting():
    selfset = {
               'main_setting': {
                   'your_name': '翊闳',
                   'awaken': 'hotword',  # 唤醒方式：语音hotword, 人脸face
                   'talk_mode': 'voice',  # 交互方式：语音交互voice，手势与文字交互gesture
                   'loc': 'china',
                   'sys_lang': 'Zh-Hans', # 你的语言：En英文/Zh-Hans普通话/Zh-Yue粤语/Zh-Chun四川话
                   'ClientId': '001',
                   'ClientType': 'xiaolan-display-client-2.0',
                   'userId': '1',
                   'url': {
                       'xiaolan_nlu': '',
                       'xiaolan_brain': '180.76.186.145'
                   },
                   'DatebaseUrl': {
                       'XiaolanSkill': '',
                       'XiaolanFace': ''
                   },
                   'STT': {
                       'service': 'tencent', #STT服务选择 百度:baidu 讯飞:ifly 腾讯：tencent（推荐腾讯，速度会快很多）
                       'baidu': {        #百度STT服务配置，AK和SK在百度云申请
                            'AK': 'TSFp0BKH547h7Agjf2WkV2Ll',
                            'SK': 'c9RZ1ZLxPe6wQVWOUwjaWOLvM7EpXHwe'
                       },
                       'ifly': {
                           'key': '',
                           'appid': ''
                       },
                       'tencent': {
                           'SI': 'AKIDOtpcw7aMZHlvx9o0m2J94KHbY0yQvxNt', # 腾讯云SecretId
                           'SK': 'GotMV9pLaNod1SbW0jY1AVEkPlEOWEjY' # 腾讯云SecretKey
                       }
                   },
                   'TTS': {
                       'service': 'baiud', #TTS服务选择 baidu youdao
                       'baidu': {        #百度TTS服务配置，AK和SK在百度云申请
                           'AK': 'TSFp0BKH547h7Agjf2WkV2Ll',
                           'SK': 'c9RZ1ZLxPe6wQVWOUwjaWOLvM7EpXHwe'
                       },
                       'youdao': {       #有道STT服务配置，appid和appkey在有道智云申请
                           'appid': '2b3bd2665750d664',
                           'appkey': 'G6E8WI8kqeixpIyQaa2cCmj3sHHsgDm8',
                           'lang': 'zh-CHS'
                       }
                   },
                   'NLU': {            #NLU语义理解服务配置
                       'ifly': {       #讯飞
                           'key': '9e1b8f6028b14b969cdec166eca127ea',
                           'appid': '5ace1bbb'
                       }
                   },
                   'NLP': {            # NLP自然语言处理引擎服务配置
                       'baidu': {      # 百度自然语言处理引擎
                           'SK': 'c9RZ1ZLxPe6wQVWOUwjaWOLvM7EpXHwe',
                           'AK': 'TSFp0BKH547h7Agjf2WkV2Ll'
                       }
                   },
                   'OCR': {            # 识别服务配置
                       'baidu': {      # 百度识别（人脸、人体、文字，物体）
                           'AK': 'TSFp0BKH547h7Agjf2WkV2Ll',
                           'SK': 'c9RZ1ZLxPe6wQVWOUwjaWOLvM7EpXHwe'
                       }
                   },
                   'Gesture': {        # 手势识别服务配置
                       'face++': {     # face++手势识别
                           'AK': '',
                           'AS': ''
                       }
                   }
               },
               'weather': {                     #天气技能，KEY在心知天气获取
                   'key': 'sxyi6ehxblxkqeto'
               },
               'tuling': {                      #图灵聊天技能，KEY,USER_ID在www.tuling123.com获取
                   'key': 'c380ed8f2880443c84892ace36ba6bad',
                   'user_id': '167031'
               },
               'news': {                        #新闻技能，KEY在阿凡达数据获取
                   'key': 'b8fff66168feb233d5cdb2f7931750f3'
               },
               'joke': {                        #说笑话技能，KEY在阿凡达数据获取
                   'key': 'a63ac25e95f741aea51167a05891498c'
               },
               'smarthome': {                   #智能家居技能，passwd，url，port在hass上
                   'passwd': 'y20050801',
                   'url': 'http://192.168.2.121',
                   'port': '8123'
               },
               'map': {                         #地图技能，key在腾讯地图API上申请
                   'key': 'FRMBZ-IREKF-MA3JI-N32XW-HXUZK-K5FUW'
               },
               'ts': {                          #翻译技能，key，appid在有道智云申请
                   'appid': '2b3bd2665750d664',
                   'key': 'G6E8WI8kqeixpIyQaa2cCmj3sHHsgDm8'
               },
               'express': {                     #快递查询技能，key，EBusinessID在快递鸟申请
                   'key': '1f0c5c35-67a8-495f-b3ab-a7fc534a826f',
                   'EBusinessID': '1349773'
               }
    }
    return selfset
