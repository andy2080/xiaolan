# -*- coding: utf-8 -*-

# description:
# author: xiaoland
# create_time: 2018/8/5

"""
    desc:pass
"""

import sys
import os
import requests
from PyQt4 import QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QLabel
sys.path.append('/home/pi/xiaolan/')
from Base import xiaolanBase

class TextDisplay(QWidget, xiaolanBase):

    def __init__(self, title, text, remind_word, background_image, remind_word_time):

        super(TextDisplay, self).__init__()
        bgi_req = requests.get(background_image)
        self.text = text
        self.title = title
        self.remind_word = remind_word
        self.remind_word_time = remind_word_time
        self.background_image = bgi_req.content
        self.text_display()

    def text_display(self):

        """
        文本展示
        :return:
        """
        self.set_background_image()
        self.set_remind_word()
        text_object = QLabel(self)
        text = self.text
        text_object.move(30, 70)
        text_object.setText(text)
        text_object.adjustSize()

    def set_remind_word(self):

        """
        设置提醒词
        :return:
        """
        remind_word = QLabel(self)
        text = self.remind_word[remind_word_time]
        remind_word.move(362, 540)
        remind_word.setText(text)
        remind_word.adjustSize()

    def set_background_image(self):

        """
        设置背景图片
        :return:
        """
        palette = QtGui.QPalette(self)
        palette.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap(self.background_image)))