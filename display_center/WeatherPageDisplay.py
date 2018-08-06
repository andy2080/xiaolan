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

class WeatherPage(QWidget, xiaolanBase):

    def __init__(self):

        super(WeatherPage, self).__init__()
        self.weather_page_display()

    def weather_page_display(self):

        """
        天气预报页面
        :return:
        """
        weather = self.set_weather()
        self.set_weather_background_image(weather)
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

    def set_remind_word(self):

        """
        设置提醒词
        :return:
        """
        remind_word = QLabel(self)
        text = self.client_to_server('get_weather_remind_word', 0)
        remind_word.move(362, 540)
        remind_word.setText(text)
        remind_word.adjustSize()

    def set_weather(self):

        """
        设置天气预报
        :return:
        """
        res = self.client_to_server('weather_page_get_weather', {'time': 'today'})
        weather_text = QLabel(self)
        remind_word.move(512, 300)
        remind_word.setText(res['WeatherText'])
        remind_word.adjustSize()
        return res['Weather']

    def set_weather_background_image(self, weather):

        """
        设置天气背景图片
        :param weather:天气类型
        :return:
        """
        if weather == 'rainy':
            image_path = '/home/pi/xiaolan/memory_center/display_image/rainy.png'
            palette3 = QtGui.QPalette(self)
            palette3.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap(image_path)))
            self.setPalette(palette3)
        elif weather == 'sunny':
            image_path = '/home/pi/xiaolan/memory_center/display_image/sunny.png'
            palette3 = QtGui.QPalette(self)
            palette3.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap(image_path)))
            self.setPalette(palette3)
        elif weather == 'cloudy':
            image_path = '/home/pi/xiaolan/memory_center/display_image/cloudy.png'
            palette3 = QtGui.QPalette(self)
            palette3.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap(image_path)))
            self.setPalette(palette3)
        else:
            image_path = '/home/pi/xiaolan/memory_center/display_image/white_cloud_bgi.png'
            palette3 = QtGui.QPalette(self)
            palette3.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap(image_path)))
            self.setPalette(palette3)