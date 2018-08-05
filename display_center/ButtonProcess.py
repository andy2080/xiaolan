# -*- coding: utf-8 -*-

import os
import sys
import datetime
import wxversion
wxversion.select("2.8-unicode")
import wx
sys.path.append('/home/pi/xiaolan/')
from BaseDisplay import BaseDisplay

class ButtonProcess(BaseDisplay):

    def __init__(self):

        super(ButtonProcess, self).__init__()

    def sleep_mode_button_process(self):

        """
        勿扰模式按钮处理
        :return:
        """

    def skill_center_button_process(self):

        """
        技能中心按钮处理
        :return:
        """

    def xiaolan_setting_process(self):

        """
        小蓝设置按钮处理
        :return:
        """