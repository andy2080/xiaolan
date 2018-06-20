# -*- coding: UTF-8 -*-

import sys
import os
sys.path.append('/home/pi/xiaolan/speech_center/')
from conversation import dialogue
sys.path.append('/home/pi/xiaolan/auditory_center/awaken/snowboy/')
import snowboydecoder


def awaken():

    detector = snowboydecoder.HotwordDetector("/home/pi/xiaolan/auditory_center/awaken/hotword/Alexa.pmdl", sensitivity=0.5, audio_gain=1)
    detector.start(a)

def a():
    try:
        sys.exit(-1)
    except SystemExit:
        d = dialogue()
        d.conversationa()

awaken()
    
