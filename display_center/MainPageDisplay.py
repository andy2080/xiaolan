# -*- coding: utf-8 -*-

# description:
# author: xiaoland
# create_time: 2018/8/5

"""
    desc:pass
"""
import sys
import os
import datetime
from PyQt5 import QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QLabel, QTime, QDateTime, QDate, QMainWindow
from PyQt5.QtGui import QIcon
sys.path.append('/home/pi/xiaolan/')
from Base import xiaolanBase

class MainPage(QWidget, xiaolanBase):

    def __init__(self):

        super(MainPage, self).__init__()
        self.main_page_display()

    def main_page_display(self):

        """
        主页
        :return:
        """
        self.set_background_image()
        self.set_remind_word()
        self.set_time()
        self.set_button()

    def set_time(self):

        """
        设置时间
        :return:
        """
        date = QDate.currentDate()
        time = QTime.currentTime()
        display_date = QLabel(self)
        display_time = QLabel(self)
        display_date.move(50, 75)
        display_date.setText(date)
        display_date.adjustSize()
        display_time.move(50, 50)
        display_time.setText(time)
        display_time.adjustSize()

    def set_button(self):

        """
        设置按钮
        :return:
        """
        # 小蓝设置按钮
        setting_button = QPushButton("", self)
        setting_button.move(904, 50)
        setting_button.pushButton.setStyleSheet('QPushButton{border-image:url(/home/pi/xiaolan/memory_center/display_image/setting.jpg)}')

        # 技能中心按钮
        setting_button = QPushButton("", self)
        setting_button.move(824, 50)
        setting_button.pushButton.setStyleSheet('QPushButton{border-image:url(/home/pi/xiaolan/memory_center/display_image/skill_center.jpg)}')

        # 帮助中心按钮
        setting_button = QPushButton("", self)
        setting_button.move(744, 50)
        setting_button.pushButton.setStyleSheet('QPushButton{border-image:url(/home/pi/xiaolan/memory_center/display_image/help_center.jpg)}')

    def set_background_image(self):

        """
        设置背景图片
        :return:
        """
        image_path = '/home/pi/xiaolan/memory_center/display_image/main_page_bgi.jpg'
        palette1 = QtGui.QPalette(self)
        palette1.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap(image_path)))
        self.setPalette(palette1)

    def set_remind_word(self):

        """
        设置提醒词
        :return:
        """
        remind_word = QLabel(self)
        text = self.client_to_server('get_remind_word', 0)
        remind_word.move(362, 540)
        remind_word.setText(text)
        remind_word.adjustSize()

