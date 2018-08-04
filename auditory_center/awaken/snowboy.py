# -*- coding: UTF-8 -*-

import sys
import os
sys.path.append('/home/pi/xiaolan/')
from Base import xiaolanBase
sys.path.append('/home/pi/xiaolan/auditory_center/awaken/snowboy/')
import snowboydecoder

class Snowboy(xiaolanBase):

    def __init__(self):

        super(Snowboy, self).__init__()

    def awaken(self):

        detector = snowboydecoder.HotwordDetector("/home/pi/xiaolan/auditory_center/awaken/hotword/jarvis.umdl,/home/pi/xiaolan/auditory_center/awaken/hotword/xiaodu_l12r10_sen_35_35_32_highsen_40_40_39_0104_kuanyang.umdl", sensitivity=[0.8, 0.8, 0.4, 0.4, 0.39], audio_gain=1, apply_frontend=True)
        detector.start(a)

def a():
    try:
        sys.exit(-1)
    except SystemExit:
        self.dialogue('conversation', 0)

    
