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

class RecommendPage(QWidget):

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

    def set_recommend_word(self):

        """
        设置推荐词
        :return:
        """

    def set_recommend_background_image(self):

        """
        设置推荐背景图片
        :return:
        """
        image_path = '/home/pi/xiaolan/memory_center/display_image/recommend_page_bgi.jpg'
        palette2 = QtGui.QPalette(self)
        palette2.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap(image_path)))
        self.setPalette(palette1)

    def set_remind_word(self):

        """
        设置推荐词
        :return:
        """
