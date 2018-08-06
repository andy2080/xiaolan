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

class SkillCenterPage(QWidget, xiaolanBase):

    def __init__(self):

        super(SkillCenterPage, self).__init__()
        self.skill_center_page_display()

    def skill_center_page_display(self):

        """
        技能中心页面
        :return:
        """

    def set_recommend_skill(self):

        """
        设置推荐技能
        :return:
        """

    def skill_page_display(self, skill):

        """
        技能介绍页面
        :param skill:
        :return:
        """

    def set_skill_center_background_image(self):

        """
        设置技能中心背景图片
        :return:
        """

    def set_skill_page_background_image(self):

        """
        设置技能介绍页面背景图片
        :return:
        """