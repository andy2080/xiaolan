# -*- coding: utf-8 -*-

import os
import sys
import json
sys.path.append('/home/pi/xiaolan/')
import setting
from Base import xiaolanBase
from learning_center.skills.smarthome import hass

class SpeacilSkills(xiaolanBase):

    def __init__(self):

        super(SpeacilSkills, self).__init__()

    def Hass(self, intentdict):

        """
        特殊技能：智能家居
        :return:
        """
        hass.start(intentidct)
