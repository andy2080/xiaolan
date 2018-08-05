# -*- coding: utf-8 -*-

import os
import sys
import wxversion
wxversion.select("2.8-unicode")
import wx
sys.path.append('/home/pi/xiaolan/')
from Base import xiaolanBase

class BaseDisplay(xiaolanBase):

    def __init__(self):

        super(BaseDisplay, self).__init__()

    def recording_display_process(self):

        """
        录制音频显示
        :return:
        """

    def main_page_display_process(self):

        """
        主页显示
        :return:
        """

    def wather_page_display_process(self):

        """
        天气页显示
        :return:
        """

    def recommend_page_display_process(self, recommend_text, remind, background_image):

        """
        推荐页显示
        :param recommend_text: 推荐文本列表三条
        :param remind: 提醒词
        :param background_image: 背景图片
        :return:
        """

    def get_main_page_background_image(self):

        """
        获取主页背景图片
        :return:
        """

    def get_recommend_page_background_image(self):

        """
        获取推荐页背景图片
        :return:
        """

    def get_weather_page_background_image(self):

        """
        获取天气页背景图片
        :return:
        """

    def get_recommend_page_text(self):

        """
        获取推荐页文本和提醒词
        :return:
        """

    def get_remind_word(self, type):

        """
        获取显示提醒词
        :param type: 哪一个展示
        :return:
        """

    def get_display_text(self, type):

        """
        获取显示文本
        :param type: 哪一个展示
        :return:
        """