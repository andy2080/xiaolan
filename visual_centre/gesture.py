# -*- coding: utf-8 -*-
# 小蓝手势识别

# description:
# author: xiaoland
# create_time: 2018/8/2

"""
    desc:pass
"""

import os
import sys
import json
import requests
import hashlib
sys.path.append('/home/pi/xiaolan/')
from Base import xiaolanBase


class Gesture(xiaolanBase):

    def __init__(self):

        super(Gesture, self).__init__()

    def start(self):

        """
        开始
        :return:
        """