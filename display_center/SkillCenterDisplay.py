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
        self.set_skill_center_background_image()
        self.set_recommend_skill()

    def set_recommend_skill(self):

        """
        设置推荐技能
        :return:
        """
        recommend_skill = self.client_to_server('get_recommend_skill', 0)
        turn = 1
        we = 30
        hi = 30
        long = len(recommend_skill)
        while 1 == 1:
            if turn == long + 1:
                break
            else:
                # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                recommend_skill_image = requests.get(recommend_skill[turn])
                palette1 = QtGui.QPalette(self)
                palette1.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap(recommend_skill_image.content)))
                palette1.move(we, hi)
                self.setPalette(palette1)
                turn += 1
                hi += 60
                # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    def skill_page_display(self, skill):

        """
        技能介绍页面
        :param skill: skill
        :return:
        """

    def set_skill_center_background_image(self):

        """
        设置技能中心背景图片
        :return:
        """
        palette = QtGui.QPalette(self)
        palette.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap(image_path)))
        self.setPalette(palette)

    def set_skill_page_background_image(self):

        """
        设置技能介绍页面背景图片
        :return:
        """