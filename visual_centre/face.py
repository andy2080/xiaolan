# -*- coding: utf-8 -*-
# 人脸唤醒

import os
import sys
import json
import requests
import base64
sys.path.append('/home/pi/xiaolan/')
from Base import xiaolanBase
sys.path.append('/home/pi/xiaolan/speech_center')
import speaker

class XiaolanFaceAwaken(xiaolanBase):

    def __init__(self):

        super(XiaolanFaceAwaken, self).__init__()



