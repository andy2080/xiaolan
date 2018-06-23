# -*- coding: utf-8 -*-

import os
import sys
import json
import demjson
import base64
import hashlib
sys.path.append('/home/pi/xiaolan')
from network_center.xiaolanClientToServer import xClientToServer
from network_center.DuerosClientToServer import dClientToServer

class CommandsList(object):
   
    def __init__(self):
        self.xc = xClientToServer
        self.dc = dClientToServer
    def GetCommandsList(self, types):
        if types == 'xiaolan':
            lists = self.xc.SendReqToServer(data)
            return lists
        elif types == 'dueros':
            lists = self.dc.SendReqToServer(url, data)
          
    
