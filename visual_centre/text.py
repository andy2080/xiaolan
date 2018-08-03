# -*- coding: utf-8 -*-
# 小蓝文字识别

# description:
# author: xiaoland
# create_time: 2018/8/3

"""
    desc:pass
"""

import sys
import os
import json
import requests
sys.path.append('/home/pi/xiaolan/')
from Base import xiaolanBase

class XiaolanTextRecognition(xiaolanBase):

    def __init__(self):

        super(XiaolanTextRecognition, self).__init__()