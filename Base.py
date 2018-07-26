# -*- coding: utf-8 -*-

# description:
# author: xiaoland
# create_time: 2018/7/19

"""
    desc:pass
"""

sys.path.append('/home/pi/xiaolan/speech_center')
import speaker
import os
import sys
import re
sys.path.append('/home/pi/xiaolan')


class xiaolanBase(object):

    def __init__(self):

        import setting
        self.set = setting.setting()

    def replace_number(self, text):

        """
        大写数字转为小写数字
        :param text: 文本
        :return:
        """
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

    def tts(self, saytext):

        """
        TTS语音合成
        :return:
        """
        from speech_center.tts import baidu_tts
        from speech_center.tts import youdao_tts
        if self.set['main_setting']['TTS']['service'] == 'baidu':
            tts = baidu_tts()
            tok = tts.get_token()
        elif self.set['main_setting']['TTS']['service'] == 'youdao':
            tts = youdao_tts()
            tok = self.set['main_setting']['TTS']['youdao']['lang']
        else:
            return {'States': 'Error:UnreadSettingForTts'}
        states = tts.tts(saytext, tok)
        speaker.speak()
        return states

    def diy_tts(self, saytext, service, more):

        """
        DIY的TTS语音合成
        :param saytext: tts文本
        :param service: tts服务
        :param more: 更多
        :return:
        """
        from speech_center.tts import baidu_tts
        from speech_center.tts import youdao_tts
        if service == 'baidu':
            tts = baidu_tts()
            tok = tts.get_token()
        elif service == 'youdao':
            tts = youdao_tts()
            tok = more['lang']

        return tts.tts(saytext, tok)



    def stt(self, path):

        """
        STT语音识别
        :param path: 语音文件
        :return:
        """
        from speech_center.stt import baidu_stt
        from speech_center.stt import ifly_stt
        if self.set['main_setting']['STT']['service'] == 'baidu':
            stt = baidu_stt()
            tok = stt.get_token()
        elif self.set['main_setting']['STT']['service'] == 'ifly':
            stt = ifly_stt()
            tok = ''
        else:
            return {'States': 'Error:UnreadSettingForStt', 'Text': 'Error'}

        text = stt.stt(path, tok)
        if text == 'None':
            speaker.speacilrecorder()
        else:
            return {'States': 'complete', 'text': self.replace_number(text.replace('，', '').replace('。', ''))}

    def face_awaken(self):

        """
        视觉唤醒（人脸唤醒）
        :return:
        """
        from visual_centre.face import XiaolanFaceAwaken
        face_awaken = XiaolanFaceAwaken()
        face_awaken.awaken()

    def log(self, mode, more):

        """
        Log记录
        :param mode: Log模式：读取/写如
        :param more: 更多
        :return:
        """
        from memory_center.Log import Log
        Log = Log()
        if mode == 'write':
            return Log.addLog(more['log'], more['level'])
        elif mode == 'read':
            return Log.Get(more)
        else:
            return {'States': 'Error:UnknowLogCommands'}

    def datebase(self, mode, more):

        """
        数据库
        :param mode: 模式
        :param more: 更多
        :return:
        """
        from memory_center.DateBase import Datebase
        Datebase = Datebase()
        if mode == 'Set':
            return Datebase.SetDate(more['date'], more['db'])
        elif mode == 'Get':
            return Datebase.GetDate(more['key'], mode['db'])
        elif mode == 'Delete':
            return Datebase.DeleteDate(more['key'], more['db'])
        elif mode == 'Replace':
            return Datebase.ReplaceDate(more['date'], more['db'])
        else:
            return {'States': 'Error:UnknowDatebaseCommands'}

    def snowboy(self):

        """
        snowboy离线唤醒引擎
        :return:
        """
        from auditory_center.awaken.snowboy import snowboy
        snowboy = snowboy()
        snowboy.awaken()

    def client_nlu(self, mode, text):

        """
        小蓝语义理解引擎
        :param mode: 模式
        :return:
        """
        from speech_center.nlu import Nlu
        Nlu = Nlu()
        if mode == 'xiaolan':
            return Nlu.xl_intent(text)
        elif mode == 'ifly':
            return Nlu.ifly_intent(text)
        else:
            return {'States': 'Error:UnkonwMode'}

    def recorder(self, mode, more):

        """
        录音
        :param mode: 模式
        :param more: 更多
        :return:
        """
        from auditory_center.recorder import recorder
        recorder = recorder()
        if mode == 'normal':
            return recorder.record()
        elif mode == 'less_time':
            return recorder.ssrecord()
        elif mode == 'translate':
            return recorder.tsrecord()
        elif mode == 'express':
            return recorder.exrecord()
        elif mode == 'Diy':
            return recorder.diy_record(more['seconds'])
        else:
            return  {'States': 'Error:UnkonwRecordMode'}

    def dialogue(self, mode, more):

        """
        对话
        :param mode:
        :param more:
        :return:
        """
        from speech_center.conversation import dialogue
        dialogue = dialogue()
        if mode == 'conversation':
            return dialogue.conversation()
        elif mode == 'wait_answer':
            return dialogue.waitAnswer(more['RecordType'])
        elif mode == 'ask_slots':
            return dialogue.AskSlots(more['SlotName'], more['SlotDicts'], more['SlotAsk'], more['RecordType'])
        else:
            return {'States': 'Error:UnknowConversationCommands'}

    def client_to_server(self, mode, more):

        """
        HTTP发送系统
        :param mode: 模式
        :param more: 更多
        :return:
        """
        from network_center.xiaolanClientToServer import ClientToServer
        ClientToServer = ClientToServer()
        if mode == 'SkillReq':
            return ClientToServer.ClientSkillReq(more['Intent'], more['Slots'], more['IntentDict'])
        elif mode == 'NluReq':

            intentdict = ClientToServer.XiaolanNluReq(more['Text'])
            if 'Error' in intentdict['Message'] or intentdict == {}:
                intentdict = self.client_nlu('xiaolan', intentdict['Text'])
                if not intentdict['Intent']:
                    intentdict['Skill'] = 'tuling'
                elif intentdict['Skill'] == 'hass':
                    self.speacil_skill('Hass', {'IntentDict': intentdict})
                else:
                    pass
            else:
                return intentdict

        elif mode == 'SkillResForWaitAnswer':
            return ClientToServer.ClientSkillResWaitAnswer(more['Intent'], more['Slots'], more['IntentDict'])
        elif mode == 'SkillResForAsklots':
            return ClientToServer.SkillAskSlotsRes(more['Slots'], more['SkillName'])
        elif mode == 'DiyReq':
            return ClientToServer.DiyReq(more['Data'])
        else:
            return {'States': 'Error:UnknowReqCommands'}

    def commands_do(self, mode, more):

        """
        小蓝大脑指令分发处理
        :param mode: 模式
        :param more: 更多
        :return:
        """
        from network_center.xiaolanServerCommandDo import CommandsDo
        CommandsDo = CommandsDo()
        if mode == 'Normal':
            return CommandsDo.Do(more['Respones'])
        else:
            return {'States': 'Error:UnknowBrainCommandsDoCommands'}

    def speacil_skill(self, skill, more):

        """
        小蓝特殊技能
        :param skill: 技能
        :param more: 更多
        :return:
        """
        from learning_center.SpeacilSkills import SpeacilSkills
        SpeacilSkills = SpeacilSkills()
        if skill == 'Hass':
            return SpeacilSkills.Hass(more['IntentDict'])
        else:
            return {'States': 'UnknowSpeacilSkillCommands'}

    def speaker(self, mode):

        """
        播音器
        :param mode: 模式
        :return:
        """
        if mode == 'ding':
            speaker.ding()
        elif mode == 'dong':
            speaker.dong()
        elif mode == 'speak':
            speaker.speak()
        elif mode == 'TextEmpty':
            speaker.speacilrecorder()
        else:
            self.log('write', {'level': 'info', 'log': 'Error:UnknowSpeakerCommands'})
            return 'Error'
