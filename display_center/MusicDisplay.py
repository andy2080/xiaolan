# -*- coding: utf-8 -*-

# description:
# author: xiaoland
# create_time: 2018/8/5

"""
    desc:pass
"""
import sys
import os
from PyQt4 import QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QLabel
sys.path.append('/home/pi/xiaolan/')
from Base import xiaolanBase

class MusicDisplay(QWidget, xiaolanBase):

    def __init__(self):

        super(MusicDisplay, self).__init__()

    def music_display(self, title, name, url, icon, background_image):

        """
        音乐展示
        :param title: 标题
        :param name: 音乐名字
        :param url: 音乐URL
        :param icon: 音乐icon
        :param background_image: 背景图片
        :return:
        """

    def set_music_player_bar(self):

        """
        设置音乐播放器控制按钮
        :return:
        """

    def set_background_image(self):

        """
        设置背景图片
        :return:
        """

    def set_music_icon(self):

        """
        设置音乐icon
        :return:
        """

    def set_remind_word(self):

        """
        设置提醒词
        :return:
        """