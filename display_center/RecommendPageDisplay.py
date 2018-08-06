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

class RecommendPage(QWidget, xiaolanBase):

    def __init__(self):

        super(RecommendPage, self).__init__()
        self.recommend_page_display()

    def recommend_page_display(self):

        """
        推荐页面
        :return:
        """
        self.set_recommend_background_image()
        self.set_recommend_word()
        self.set_remind_word()
        # 小蓝设置按钮
        setting_button = QPushButton("", self)
        setting_button.move(904, 50)
        setting_button.pushButton.setStyleSheet(
            'QPushButton{border-image:url(/home/pi/xiaolan/memory_center/display_image/setting.png)}')

        # 技能中心按钮
        setting_button = QPushButton("", self)
        setting_button.move(824, 50)
        setting_button.pushButton.setStyleSheet(
            'QPushButton{border-image:url(/home/pi/xiaolan/memory_center/display_image/skill_center.png)}')

        # 帮助中心按钮
        setting_button = QPushButton("", self)
        setting_button.move(744, 50)
        setting_button.pushButton.setStyleSheet(
            'QPushButton{border-image:url(/home/pi/xiaolan/memory_center/display_image/help_center.png)}')

    def set_recommend_word(self):

        """
        设置推荐词
        :return:
        """
        recommend_list = self.client_to_server('get_recommend_word', 0)
        recommend_word1 = QLabel(self)
        recommend_word1.move(512, 300)
        recommend_word1.setText(recommend_list[0])
        recommend_word1.adjustSize()
        recommend_word2 = QLabel(self)
        recommend_word2.move(487, 300)
        recommend_word2.setText(recommend_list[1])
        recommend_word2.adjustSize()
        recommend_word3 = QLabel(self)
        recommend_word3.move(537, 300)
        recommend_word3.setText(recommend_list[2])
        recommend_word3.adjustSize()


    def set_recommend_background_image(self):

        """
        设置推荐背景图片
        :return:
        """
        image_path = '/home/pi/xiaolan/memory_center/display_image/recommend_page_bgi.png'
        palette2 = QtGui.QPalette(self)
        palette2.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap(image_path)))
        self.setPalette(palette1)

    def set_remind_word(self):

        """
        设置推荐词
        :return:
        """
        remind_word = QLabel(self)
        text = self.client_to_server('get_recommend_remind_word', 0)
        remind_word.move(362, 540)
        remind_word.setText(text)
        remind_word.adjustSize()
