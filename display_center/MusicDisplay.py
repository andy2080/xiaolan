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

class MusicDisplay(QWidget, xiaolanBase):

    def __init__(self, title, name, remind, icon, background_image, remind_word_time):

        super(MusicDisplay, self).__init__()
        bgi_req = requests.get(background_image)
        icon_req = requests.get(icon)
        self.background_image = bgi_req.content
        self.remind = remind
        self.icon = icon_req.content
        self.remind_word_time = remind_word_time
        self.name = name
        self.title = title
        self.music_display()

    def music_display(self):

        """
        音乐展示
        :return:
        """
        self.set_background_image()
        self.set_music_player_bar()
        self.set_remind_word()
        self.set_music_icon()

    def set_music_player_bar(self):

        """
        设置音乐播放控制器
        :return:
        """

    def set_background_image(self):

        """
        设置背景图片
        :return:
        """
        palette = QtGui.QPalette(self)
        palette.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap(self.background_image)))
        palette.move(0, 0)
        self.setPalette(palette)

    def set_music_icon(self):

        """
        设置音乐icon
        :return:
        """
        photo = QPixmap()
        photo.loadFromData(self.icon)
        icon = QLabel()
        icon.setPixmap(photo)
        icon.move(341, 200)

    def set_remind_word(self):

        """
        设置提醒词
        :return:
        """
        remind_word = QLabel(self)
        text = self.remind[self.remind_word_time]
        remind_word.move(362, 540)
        remind_word.setText(text)
        remind_word.adjustSize()