# -*- coding: utf-8 -*-

# description:
# author: xiaoland
# create_time: 2018/7/19

"""
    desc:pass
"""
import sys
sys.path.append('/home/pi/xiaolan/speech_center')
import speaker
import os
import requests
import re
import ctypes
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
            tts = baidu_tts()
            tok = tts.get_token()
            self.log('write', {'log': 'Error:UnreadSettingForTTS', 'level': 'waring'})

        self.log('write', {'log': 'StartTTS:' + saytext, 'level': 'info'})
        states = tts.tts_start(saytext, tok)
        if 'Error' in states:
            self.log('write', {'log': states['States'], 'level': 'error'})
        else:
            speaker.speak()

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
        else:
            tok = tts.get_token()
            tts = baidu_tts()

        self.log('write', {'log': 'StartTTS:' + saytext, 'level': 'info'})
        states = tts.tts_start(saytext, tok)
        if 'Error' in states['States']:
            self.log('write', {'log': states['States'], 'level': 'error'})
        else:
            speaker.speak()



    def stt(self, path):

        """
        STT语音识别
        :param path: 语音文件
        :return:
        """
        from speech_center.stt import baidu_stt
        from speech_center.stt import ifly_stt
        from speech_center.stt import ActualTimeStt
        if self.set['main_setting']['STT']['service'] == 'baidu':
            stt = baidu_stt()
            tok = stt.get_token()
        elif self.set['main_setting']['STT']['service'] == 'ifly':
            stt = ifly_stt()
            tok = ''
        else:
            self.log('write', {'log': 'BaseSTTUnkonwCommands', 'level': 'warning'})
            return None

        self.log('write', {'log': 'StartSTT', 'level': 'info'})
        states = stt.stt_starts(path, tok)
        if 'Error' in states['States']:
            self.log('write', {'log': 'Error:BaseStt:' + states['States']})
            return None
        else:
            text = 'a'
            a = 0
            i = len(states['Text'])
            while 1 == 1:
                try:
                    text = text + states['Text'][a]
                except IndexError:
                    break
                else:
                    a += 1
            text = text[1:-1]
            print "YourSttResult:" + text
            if text == 'None':
                self.log('write', {'log': 'BaseSTTTextNone', 'level': 'debug'})
                speaker.speacilrecorder()
            else:
                self.log('write', {'log': 'BaseSTTComplete' + text, 'level': 'debug'})
                f = open('/home/pi/xiaolan/memory_center/more/text.txt', "w")
                f.write(self.replace_number(text.replace('，', '').replace('。', '')))
                f.close()

    def face_awaken(self, mode):

        """
        视觉唤醒（人脸唤醒）
        :param mode: 更多
        :return:
        """
        from visual_centre.face import XiaolanFaceAwaken
        face_awaken = XiaolanFaceAwaken()
        if mode == 'awaken':

            self.log('write', {'log': 'Event:XiaolanFaceAwakenStart', 'level': 'info'})
            face_awaken.awaken()
        elif mode == 'all_new_sign_up':

            face_awaken.all_new_sign_up_face()

    def snowboy(self):

        """
        snowboy离线唤醒引擎
        :return:
        """
        from auditory_center.awaken.snowboy import Snowboy
        snowboy = Snowboy()
        self.log('write', {'log': 'Event:SnowboyVoiceAwakenStart', 'level': 'info'})
        snowboy.awaken()

    def log(self, mode, more):

        """
        Log记录
        :param mode: Log模式：读取/写如
        :param more: 更多
        :return:
        """
        from memory_center.Log import Log
        log = Log()
        if mode == 'write':
            log.add_log(more['log'], more['level'])
        elif mode == 'read':
            log.get(more['mode'])
        else:
            self.log('write', {'log': 'BaseLogError:UnknowLogCommands', 'level': 'wraning'})

    def datebase(self, mode, more):

        """
        数据库
        :param mode: 模式
        :param more: 更多
        :return:
        """
        from memory_center.DateBase import Datebase
        datebase = Datebase()
        if mode == 'Set':

            self.log('write', {'log': 'DatebaseWrite:' + more['date'] + 'In' + more['db']})
            states = datebase.set_date(more['date'], more['db'])
            if 'Error' in states['States']:
                self.log('write', {'log': 'Error:DatebaseSetDateFaild:' + states['States'], 'level': 'warning'})
            else:
                self.log('write', {'log': 'Complete:DatebaseSetDateComplete', 'level': 'debug'})

        elif mode == 'Get':

            self.log('write', {'log': 'DatebaseGet:' + more['key'] + 'In' + more['db']})
            states = datebase.get_date(more['key'], mode['db'])
            if 'Error' in states['States']:
                self.log('write', {'log': 'Error:DatebaseSetDateFaild:' + states['States'], 'level': 'warning'})
            else:
                self.log('write', {'log': 'Complete:DatebaseSetDateComplete', 'level': 'debug'})

        elif mode == 'Delete':

            self.log('write', {'log': 'DatebaseDelete:' + more['key'] + 'In' + more['db']})
            states = datebase.delete_date(more['key'], more['db'])
            if 'Error' in states['States']:
                self.log('write', {'log': 'Error:DatebaseSetDateFaild:' + states['States'], 'level': 'warning'})
            else:
                self.log('write', {'log': 'Complete:DatebaseSetDateComplete', 'level': 'debug'})

        elif mode == 'Replace':

            self.log('write', {'log': 'DatebaseReplace:' + more['date'][0] + ',Date' + more['date'][1] + 'In' + more['db']})
            states = datebase.replace_date(more['date'], more['db'])
            if 'Error' in states['States']:
                self.log('write', {'log': 'Error:DatebaseSetDateFaild:' + states['States'], 'level': 'warning'})
            else:
                self.log('write', {'log': 'Complete:DatebaseSetDateComplete', 'level': 'debug'})

        else:

            self.log('write', {'log': 'Error:UnknowCommandsForBaseDatebase', 'level': 'warning'})

    def client_nlu(self, mode, text):

        """
        小蓝语义理解引擎
        :param mode: 模式
        :param text: 文本
        :return:
        """
        from speech_center.nlu import nlu
        nlu = nlu()
        if mode == 'xiaolan':

            states = nlu.xl_intent(text)
            if 'Error' in states['States']:
                self.log('write', {'log': 'Error:XiaolanClientIntentDoError:' + states['States'], 'level': 'error'})
            else:
                self.log('write', {'log': 'XiaolanClientIntentDoComplete', 'level': 'debug'})

        elif mode == 'get_slots':

            states = nlu.get_slots(more['SlotsList'], more['Text'])
            if 'Error' in states['States']:
                self.log('write', {'log': 'Error:XiaolanClientNluGetSlotsError:' + states['States'], 'level': 'warning'})
                return states
            else:
                self.log('write', {'log': 'Complete:XiaolanClientNluGetSlotsComplete', 'level': 'debug'})
                return states

        elif mode == 'ifly':

            states = nlu.ifly_intent(text)
            if 'Error' in states['States']:
                self.log('write', {'log': 'Error:IflyIntentDoError:' + states['States'], 'level': 'error'})
            else:
                self.log('write', {'log': 'IflyIntentDoComplete', 'level': 'debug'})

        else:

            self.log('write', {'log': 'Error:UnknowBaseLogCommands', 'level': 'warning'})

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

            self.log('write', {'log': 'Event:StartNormalRecording', 'level': 'info'})
            recorder.record()
        elif mode == 'less_time':

            self.log('write', {'log': 'Event:StartLess_TimeRecording', 'level': 'info'})
            recorder.ssrecord()
        elif mode == 'translate':

            self.log('write', {'log': 'Event:StartTranslateRecording', 'level': 'info'})
            recorder.tsrecord()
        elif mode == 'express':

            self.log('write', {'log': 'Event:StartExpressRecording', 'level': 'info'})
            recorder.exrecord()
        elif mode == 'Diy':

            self.log('write', {'log': 'Event:StartDiyRecordingFor' + more['seconds'] + 's', 'level': 'info'})
            recorder.diy_record(more['seconds'])
        else:

            self.log('write', {'log': 'Error:UnkonwRecordMode', 'level': 'warning'})

    def dialogue(self, mode, more):

        """
        对话
        :param mode: 模式
        :param more: 更多
        :return:
        """
        from speech_center.conversation import Dialogue
        dialogue = Dialogue()
        if mode == 'conversation':

            self.log('write', {'log': 'Event:StartConversation', 'level': 'info'})
            dialogue.conversation()
        elif mode == 'wait_answer':

            self.log('write', {'log': 'Event:StartProcessingWaitAnswer', 'level': 'info'})
            dialogue.wait_answer(more['RecordType'])
        elif mode == 'ask_slots':

            self.log('write', {'log': 'Event:StartProcessingAskSlots', 'level': 'info'})
            dialogue.ask_slots(more['SlotNames'], more['SlotDicts'], more['SlotAsks'], more['RecordTypes'])
        else:

            self.log('write', {'log': 'Error:UnknowConversationCommands', 'level': 'warning'})

    def client_to_server(self, mode, more):

        """
        HTTP发送系统
        :param mode: 模式
        :param more: 更多
        :return:
        """
        from network_center.xiaolanClientToServer import ClientToServer
        client_to_server = ClientToServer()
        if mode == 'SkillReq':

            self.log('write', {'log': 'Event:XiaolanBrainRequestsStart', 'level': 'info'})
            states = client_to_server.client_skill_req(more['Intent'], more['Slots'], more['IntentDict'])
        elif mode == 'NluReq':

            self.log('write', {'log': 'Event:XiaolanNluRequestsStart', 'level': 'info'})
            intentdict = client_to_server.xiaolan_nlu_req(more['Text'])
            if 'Error' in intentdict['States'] or not intentdict:

                self.log('write', {'log': 'Error:XiaolanClientRequestsXiaolanNluProcessingEngineError', 'level': 'error'})
                intentdict = self.client_nlu('xiaolan', intentdict['Text'])
                if not intentdict['Intent']:

                    self.log('write', {'log': 'Warning:IntentNull', 'level': 'warning'})
                    intentdict['Skill'] = 'tuling'
                elif intentdict['Skill'] == 'hass':

                    self.log('write', {'log': 'SpeacilSkill:Hass', 'level': 'debug'})
                    self.speacil_skill('Hass', {'IntentDict': intentdict})
                else:

                    pass
            else:
                self.log('write', {'log': 'Complete:XiaolanClientRequestsXiaolanNluProcessingEngineComplete', 'level': 'debug'})
                return intentdict

        elif mode == 'SkillResForWaitAnswer':

            self.log('write', {'log': 'Event:XiaolanSkillRequestsForSkillWaitAnswerResponesStart', 'level': 'info'})
            states = client_to_server.client_skill_res_wait_answer(more['Intent'], more['Slots'], more['IntentDict'])
            if 'Error' in states['States']:
                self.log('write', {'log': 'Error:XiaolanSkillRequestsForSkillWaitAnswerResponesError:' + states['States'], 'level': 'error'})
            else:
                self.log('write', {'log': 'Complete:XiaolanSkillRequestsForSkillWaitAnswerResponesComplete', 'level': 'debug'})
        elif mode == 'SkillResForAskSlots':

            self.log('write', {'log': 'Event:XiaolanSkillRequestsForSkillAskSlotsResponesStart', 'level': 'info'})
            states = client_to_server.skill_ask_slots_res(more['Slots'], more['SkillName'])
            if 'Error' in states['States']:
                self.log('write', {'log': 'Error:XiaolanSkillRequestsForSkillAskSlotsResponesError:' + states['States'], 'level': 'error'})
            else:
                self.log('write', {'log': 'Complete:XiaolanSkillRequestsForSkillAskSlotsResponesComplete', 'level': 'debug'})
        elif mode == 'DiyReq':

            self.log('write', {'log': 'Event:DiyRequestsStart', 'level': 'info'})
            states = client_to_server.diy_req(more['Data'])
        elif mode == 'LogResForBrain':

            self.log('write', {'log': 'Event:StartSendLogToXiaolanBrain'})
        else:
            self.log('write', {'log': 'Error:UnknowRequestsCommands', 'level': 'warning'})

    def commands_do(self, mode, more):

        """
        小蓝大脑指令分发处理
        :param mode: 模式
        :param more: 更多
        :return:
        """
        from network_center.xiaolanServerCommandDo import CommandsDo
        commands_do = CommandsDo()
        if mode == 'Normal':

            self.log('write', {'log': 'Event:StartServerProcessing', 'level': 'info'})
            states = commands_do.process(more['Respones'])
            if 'Error' in states['States']:
                self.log('write', {'log': 'Error:XiaolanBrainCommandsProcessingError', 'level': 'error'})
            else:
                pass
        else:
            self.log('write', {'log': 'Error:UnknowBrainCommandsDoCommands', 'level': 'warning'})

    def speacil_skill(self, skill, more):

        """
        小蓝特殊技能
        :param skill: 技能
        :param more: 更多
        :return:
        """
        from learning_center.SpeacilSkills import SpeacilSkills
        speacil_skills = SpeacilSkills()
        if skill == 'Hass':
            return speacil_skill.Hass(more['IntentDict'])
        else:
            return {'States': 'UnknowSpeacilSkillCommands'}

    def speaker(self, mode):

        """
        播音器
        :param mode: 模式
        :return:
        """
        if mode == 'ding':
            self.log('write', {'log': 'XiaolanSpeakerEvent:StartRecording', 'level': 'info'})
            speaker.ding()
        elif mode == 'dong':
            self.log('write', {'log': 'XiaolanSpeakerEvent:RecordingComplete', 'level': 'info'})
            speaker.dong()
        elif mode == 'speak':
            self.log('write', {'log': 'XiaolanSpeakerEvent:Speak', 'level': 'info'})
            speaker.speak()
        elif mode == 'TextEmpty':
            self.log('write', {'log': 'XiaolanSpeakerEvent:TextNull', 'level': 'info'})
            speaker.speacilrecorder()
        else:
            self.log('write', {'log': 'Error:UnknowSpeakerCommands', 'level': 'warning'})

    def display(self, mode, more):

        """
        显示
        :param mode: 模式
        :param more: 更多
        :return:
        """

        from display_center.display import ScreenDisplay
        display = ScreenDisplay()
        if mode == 'video_display':

            self.log('write', {'log': 'Event:ScreeVideoDisplay', 'level': 'info'})