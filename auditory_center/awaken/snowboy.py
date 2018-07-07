# -*- coding: UTF-8 -*-

import sys
import os
sys.path.append('/home/pi/xiaolan/speech_center/')
from conversation import dialogue
sys.path.append('/home/pi/xiaolan/auditory_center/awaken/snowboy/')
import snowboydecoder


def awaken():

    detector = snowboydecoder.HotwordDetector("/home/pi/xiaolan/auditory_center/awaken/hotword/jarvis.umdl,/home/pi/xiaolan/auditory_center/awaken/hotword/xiaodu_l12r10_sen_35_35_32_highsen_40_40_39_0104_kuanyang.umdl", sensitivity=[0.8, 0.8, 0.4, 0.4, 0.39], audio_gain=1, apply_frontend=True)
    detector.start(a)

def a():
    try:
        sys.exit(-1)
    except SystemExit:
        d = dialogue()
        d.conversationa()

awaken()
    
