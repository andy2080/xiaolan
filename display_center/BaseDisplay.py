# -*- coding: utf-8 -*-

import os
import sys
import wx
sys.path.append('/home/pi/xiaolan/')
from Base import xiaolanBase

class BaseDisplay(xiaolanBase):

    def __init__(self):

        super(BaseDisplay, self).__init__()

    def recording_display(self):

        """
        录制音频显示
        :return:
        """

    def main_page_display(self):

        """
        主页显示
        :return:
        """

    def wather_page_display(self):

        """
        天气页显示
        :return:
        """

    def recommend_page_display(self, recommend_text, remind, background_image):

        """
        推荐页显示
        :param recommend_text: 推荐文本列表三条
        :param remind: 提醒词
        :param background_image: 背景图片
        :return:
        """

    def get_main_page_backgound_image(self):

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