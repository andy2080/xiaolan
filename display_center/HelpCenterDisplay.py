# -*- coding: utf-8 -*-

# description:
# author: xiaoland
# create_time: 2018/8/6

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

class HelpCenterPage(QWidget, xiaolanBase):

    def __init__(self):

        super(HelpCenterPage, self).__init__()
        self.help_center_page_display()

    def help_center_page_display(self):

        """
        帮助中心页面
        :return:
        """

    def set_help_center_question(self):

        """
        设置帮助中心的常见问题
        :return:
        """

    def set_help_center_background_image(self):

        """
        设置帮助中心背景图片
        :return:
        """