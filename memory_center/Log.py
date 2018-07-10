# -*- coding: utf-8 -*-
# LOG

import sys
import os
import requests
import json
import base64
import logging
import os.path
import time

class Log(object):

    def __init__(self):
        pass
    def Get(self):
        pass
    def addLog(self, log, level):
        # 第一步，创建一个logger
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)  # Log等级总开关
        # 第二步，创建一个handler，用于写入日志文件
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        log_path = os.path.dirname(os.getcwd()) + '/home/pi/xiaolan/memory_center/'
        log_name = 'xiaolan' + '.log'
        logfile = log_name
        fh = logging.FileHandler(logfile, mode='w')
        fh.setLevel(logging.DEBUG)
        # 第三步，定义handler的输出格式
        formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
        fh.setFormatter(formatter)
        # 第四步，将logger添加到handler里面
        logger.addHandler(fh)