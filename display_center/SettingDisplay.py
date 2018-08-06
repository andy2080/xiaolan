# -*- coding: utf-8 -*-

# description:
# author: xiaoland
# create_time: 2018/8/5

"""
    desc:pass
"""
import os
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QLabel
from PyQt4 import QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import *
sys.path.append('/home/pi/xiaolan/')
from Base import xiaolanBase

class SettingPage(QWidget, xiaolanBase):

    def __init__(self):

        super(SettingPage, self).__init__()

    def setting_page_display(self):

        """
        设置页面
        :return:
        """

    def set_setting_button(self):

        """
        设置设置按钮
        :return:
        """