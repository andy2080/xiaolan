# -*- coding: utf-8 -*-
# 人脸唤醒

import os
import sys
import json
import requests
import base64
import ctypes
sys.path.append('/home/pi/xiaolan/')
from Base import xiaolanBase
sys.path.append('/home/pi/xiaolan/speech_center')
import speaker

class XiaolanFaceAwaken(xiaolanBase):

    def __init__(self):

        super(XiaolanFaceAwaken, self).__init__()
        self.ll = ctypes.cdll.LoadLibrary

    def baidu_face_track_image(self, path):

        """
        百度人脸检测图片（离线）
        :return:
        """
        lib = self.ll('./visual_centre/baidu_face_api_linux_c++/cpp/xiaolan_face.so')
        return lib.xiaolan_face_track_image(path)

    def baidu_face_track_camera(self):

        """
        百度人脸检测实时（离线）
        :return:
        """
        lib = self.ll('./visual_centre/baidu_face_api_linux_c++/cpp/xiaolan_face.so')
        f = open('/home/pi/xiaolan/memory_center/more/face_track.txt', "w")
        f.write(lib.xiaolan_face_track_video())
        f.close()

    def baidu_face_match(self, imgf, imgs):

        """
        百度人脸对比（离线）
        :return:
        """
        lib = self.ll('./visual_centre/baidu_face_api_linux_c++/cpp/xiaolan_face.so')
        return lib.xiaolan_face_match(imgf, imgs)

    def all_new_sign_up_face(self):

        """
        人脸注册
        :return:
        """
        self.log('write', {'log': 'Event:StartAllNewSignUpFace', 'level': 'info'})
        self.tts("您好！欢迎使用小蓝！您选择了人脸唤醒，现在开始帮您注册人脸，请将人脸对准摄像头")
        os.system('raspistill -o /home/pi/xiaolan/memory_center/face_img/face_datebase/main.jpg')
        if self.baidu_face_track(path) > 0:
            self.tts("好的，注册完毕，您希望我称呼您为什么呢？")
            self.speaker('ding')
            self.recorder('normal', 0)
            self.speaker('dong')
            name = self.stt('./voice.wav')
            users_name = self.datebase('Get', {'key': 'XiaolanFaceUsers', 'db': 'XiaolanFace'})
            while 1 == 1:
                if name in user_name.read():
                    self.tts("这个称呼已经有了，换一个吧")
                    self.speaker('ding')
                    self.recorder('normal', 0)
                    self.speaker('dong')
                    name = self.stt('./voice.wav')
                else:
                    new_face_users = users_name.append(name)
                    self.datebase('Replace', {'date': ['XiaolanFaceUsers', new_face_users], 'db': 'XiaolanFace'})
                    break
            os.rename("./memory_center/face_img/face_datebase/main.jpg", name + '.jpg')
            img = open("./memory_center/face_img/face_datebase/main.jpg", name + '.jpg', "r")
            imgs = base64.b64encode(img.read())
            img.close()
            ago_face_users = self.datebase('Get', {'key': 'XiaolanFaceUsers', 'db': 'XiaolanFace'})
            ago_face_users[name] = imgs
            self.datebase('Replace', {'date': ['XiaolanFaceUsers', ago_face_users], 'db': 'XiaolanFace'})

    def new_sign_up_face(self):

        """
        人脸注册
        :return:
        """
        self.log('write', {'log': 'Event:StartSingUpNewFace', 'level': 'info'})
        self.tts("您好！我是小蓝，我似乎不认识您，但是我一定会为您尽心尽力的服务的！接下来，我会为您拍一张照，作为视觉唤醒的图片，请把脸对准摄像头")
        os.system('raspistill -o /home/pi/xiaolan/memory_center/face_img/face_datebase/main.jpg')
        if self.baidu_face_track(path) > 0:
            self.tts("好的，拍完了，真好看，您希望我称呼您为什么呢？")
            self.speaker('ding')
            self.recorder('normal', 0)
            self.speaker('dong')
            name = self.stt('./voice.wav')
            user_name = self.datebase('Get', {'key': 'XiaolanFaceUsers', 'db': 'XiaolanFace'})
            while 1 == 1:
                if name in user_name:
                    self.tts("这个称呼已经有了，换一个吧")
                    self.speaker('ding')
                    self.recorder('normal', 0)
                    self.speaker('dong')
                    name = self.stt('./voice.wav')
                else:
                    new_face_users = user_name.append(name)
                    self.datebase('Replace', {'date': ['XiaolanFaceUsers', new_face_users], 'db': 'XiaolanFace'})
                    break
            os.rename("./memory_center/face_img/face_datebase/main.jpg", name + '.jpg')
            img = open("./memory_center/face_img/face_datebase/main.jpg", name + '.jpg', "r")
            imgs = base64.b64encode(img.read())
            img.close()
            ago_face_users = self.datebase('Get', {'key': 'XiaolanFaceUsersDate', 'db': 'XiaolanFace'})
            ago_face_users[name] = imgs
            self.datebase('Replace', {'date': ['XiaolanFaceUsersDate', ago_face_users], 'db': 'XiaolanFace'})

    def awaken(self):

        """
        人脸唤醒主要逻辑（视觉唤醒）
        :return:
        """
        f = open('/home/pi/xiaolan/memory_center/more/face_track.txt', "r")
        while 1 == 1:
            if int(f.read()) > 0:
                while 1 == 1:
                    os.system('raspistill -o /home/pi/xiaolan/memory_center/face_img/face.jpg')
                    face_num = self.baidu_face_track_image('/home/pi/xiaolan/memory_center/face_img/face.jpg')
                    lib = self.ll('./visual_centre/baidu_face_api_linux_c++/cpp/xiaolan_face.so')
                    result = json.loads(lib.xiaolan_face_quality('/home/pi/xiaolan/memory_center/face_img/face.jpg'))
                    print result
                    if int(result['score']) > 0.49:
                        if int(result['Occl_chin']) > 0.49 or int(result['Occl_Occl_r_contour']) > 0.49 or int(
                                result['Occl_l_contour']) > 0.49 or int(result['Occl_l_eye']) > 0.49 or int(
                                result['Occl_r_eye']) > 0.49:
                            pass
                        else:
                            if face_num > 0:
                                face_users_img_date = self.datebase('Get', {'key': 'XiaolanFaceUsersDate',
                                                                            'db': 'XiaolanFace'})
                                face_users = self.datebase('Get', {'key': 'XiaolanFaceUsers', 'db': 'XiaolanFace'})
                                trun = 0
                                while 1 == 1:
                                    imgf = '/home/pi/xiaolan/memory_center/face_img/face.jpg'
                                    name = face_users[trun]
                                    imgs = face_users_img_date[name]
                                    result = self.baidu_face_match(imgf, imgs)
                                    result = json.loads(result)
                                    print result
                                    if result['score'] > 49.5:
                                        self.tts(name + '，有什么我可以帮到您的吗？')
                                        self.dialogue('conversation', 0)
                                        break
                                    else:
                                        try:
                                            face_users[trun + 1]
                                        except IndexError:
                                            self.new_sign_up_face()
                                            self.dialogue('conversation', 0)
                                            break
                                        else:
                                            trun = trun + 1
                            else:
                                pass
                    else:
                        pass
            else:
                pass
        f.close()

















