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
            self.log('write', {'log': 'Error:UnreadSettingForTTS', 'level': 'waring'})

        self.log('write', {'log': 'StartTTS:' + saytext, 'level': 'info'})
        states = tts.tts(saytext, tok)
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

        self.log('write', {'log': 'StartTTS:' + saytext, 'level': 'info'})
        states = tts.tts(saytext, tok)
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
        states = stt.stt(path, tok)
        if 'Error' in states['States']:
            self.log('write', {'log': 'Error:BaseStt:' + states['States']})
            return None
        else:
            if states['Text'] == 'None':
                self.log('write', {'log': 'BaseSTTTextNone', 'level': 'debug'})
                speaker.speacilrecorder()
            else:
                self.log('write', {'log': 'BaseSTTComplete' + states['Text'], 'level': 'debug'})
                return self.replace_number(text.replace('，', '').replace('。', ''))

    def face_awaken(self):

        """
        视觉唤醒（人脸唤醒）
        :return:
        """
        from visual_centre.face import XiaolanFaceAwaken
        face_awaken = XiaolanFaceAwaken()
        self.log('write', {'log': 'Event:XiaolanFaceAwakenStart', 'level': 'info'})
        face_awaken.awaken()

    def snowboy(self):

        """
        snowboy离线唤醒引擎
        :return:
        """
        from auditory_center.awaken.snowboy import snowboy
        snowboy = snowboy()
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
        Log = Log()
        if mode == 'write':
            Log.addLog(more['log'], more['level'])
        elif mode == 'read':
            Log.Get(more['mode'])
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
        Datebase = Datebase()
        if mode == 'Set':

            self.log('write', {'log': 'DatebaseWrite:' + more['date'] + 'In' + more['db']})
            states = Datebase.SetDate(more['date'], more['db'])
            if 'Error' in states['States']:
                self.log('write', {'log': 'Error:DatebaseSetDateFaild:' + states['States'], 'level': 'warning'})
            else:
                self.log('write', {'log': 'Complete:DatebaseSetDateComplete', 'level': 'debug'})

        elif mode == 'Get':

            self.log('write', {'log': 'DatebaseGet:' + more['key'] + 'In' + more['db']})
            states = Datebase.GetDate(more['key'], mode['db'])
            if 'Error' in states['States']:
                self.log('write', {'log': 'Error:DatebaseSetDateFaild:' + states['States'], 'level': 'warning'})
            else:
                self.log('write', {'log': 'Complete:DatebaseSetDateComplete', 'level': 'debug'})

        elif mode == 'Delete':

            self.log('write', {'log': 'DatebaseDelete:' + more['key'] + 'In' + more['db']})
            states = Datebase.DeleteDate(more['key'], more['db'])
            if 'Error' in states['States']:
                self.log('write', {'log': 'Error:DatebaseSetDateFaild:' + states['States'], 'level': 'warning'})
            else:
                self.log('write', {'log': 'Complete:DatebaseSetDateComplete', 'level': 'debug'})

        elif mode == 'Replace':

            self.log('write', {'log': 'DatebaseReplace:' + more['date'][0] + ',Date' + more['date'][1] + 'In' + more['db']})
            states = Datebase.ReplaceDate(more['date'], more['db'])
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
        :return:
        """
        from speech_center.nlu import Nlu
        Nlu = Nlu()
        if mode == 'xiaolan':

            states = Nlu.xl_intent(text)
            if 'Error' in states['States']:
                self.log('write', {'log': 'Error:XiaolanClientIntentDoError:' + states['States'], 'level': 'error'})
            else:
                self.log('write', {'log': 'XiaolanClientIntentDoComplete', 'level': 'debug'})

        elif mode == 'get_slots':

            states = Nlu.get_slots(more['SlotsList'], more['Text'])
            if 'Error' in states['States']:
                self.log('write', {'log': 'Error:XiaolanClientNluGetSlotsError:' + states['States'], 'level': 'warning'})
                return states
            else:
                self.log('write', {'log': 'Complete:XiaolanClientNluGetSlotsComplete', 'level': 'debug'})
                return states

        elif mode == 'ifly':

            states = Nlu.ifly_intent(text)
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
        from speech_center.conversation import dialogue
        dialogue = dialogue()
        if mode == 'conversation':

            self.log('write', {'log': 'Event:StartConversation', 'level': 'info'})
            dialogue.conversation()
        elif mode == 'wait_answer':

            self.log('write', {'log': 'Event:StartProcessingWaitAnswer', 'level': 'info'})
            dialogue.waitAnswer(more['RecordType'])
        elif mode == 'ask_slots':

            self.log('write', {'log': 'Event:StartProcessingAskSlots', 'level': 'info'})
            dialogue.AskSlots(more['SlotNames'], more['SlotDicts'], more['SlotAsks'], more['RecordTypes'])
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
        ClientToServer = ClientToServer()
        if mode == 'SkillReq':

            self.log('write', {'log': 'Event:XiaolanBrainRequestsStart', 'level': 'info'})
            states = ClientToServer.ClientSkillReq(more['Intent'], more['Slots'], more['IntentDict'])
        elif mode == 'NluReq':

            self.log('write', {'log': 'Event:XiaolanNluRequestsStart', 'level': 'info'})
            intentdict = ClientToServer.XiaolanNluReq(more['Text'])
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
            return ClientToServer.ClientSkillResWaitAnswer(more['Intent'], more['Slots'], more['IntentDict'])
        elif mode == 'SkillResForAskSlots':

            self.log('write', {'log': 'Event:XiaolanSkillRequestsForSkillAskSlotsResponesStart', 'level': 'info'})
            return ClientToServer.SkillAskSlotsRes(more['Slots'], more['SkillName'])
        elif mode == 'DiyReq':

            self.log('write', {'log': 'Event:DiyRequestsStart', 'level': 'info'})
            return ClientToServer.DiyReq(more['Data'])
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
        CommandsDo = CommandsDo()
        if mode == 'Normal':

            self.log('write', {'log': 'Event:StartServerProcessing', 'level': 'info'})
            states = CommandsDo.Do(more['Respones'])
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
