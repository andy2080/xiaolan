# -*- coding: utf-8 -*-

import os
import sys
import json
import wx


sys.path.append('/home/pi/xiaolan/')
from Base import xiaolanBase

class ScreenDisplay(xiaolanBase):
    
    def __init__(self):

        super(ScreenDisplay, self).__init__()

    def text_display_process(self, title, text, remind, background_image):

        """
        文字展示
        :param title: 标题
        :param text: 文字
        :param remind: 提醒词列表
        :param background_image: 背景图片
        :return:
        """

    def video_display_process(self, title, url, remind):

        """
        视频播放
        :param url: 视频url列表
        :param remind: 提醒词列表
        :param title: 标题
        :return:
        """

    def music_display_process(self, title, url, remind, background_image):

        """
        音乐播放
        :param title: 标题
        :param url: 音乐url列表
        :param remind: 提醒词列表
        :param background_image: 背景图片
        :return:
        """

    def image_display_process(self, title, url, remind):

        """
        图片展示
        :param title: 标题
        :param url: 图片url列表
        :param remind: 提醒词列表
        :return:
        """

    def list_display_rocess(self, type, title, list_info, remind, background_image):

        """
        列表显示
        :param type: 类型 transverse,vertical
        :param title: 标题
        :param list_info: 列表信息
        :param remind: 提醒词
        :param background_image: 背景图片URL
        :return:
        """

    def standard_display(self, title, image, text, remind, background_image):

        """
        标准显示
        :param title: 标题
        :param image: 图片信息
        :param remind: 提醒词
        :param text: 文本
        :param background_image: 背景图片
        :return:
        """

    def left_image_right_text_display_process(self, title, image, text, remind, background_image):

        """
        左图右文显示
        :param title: 标题
        :param image: 图片
        :param text: 文字
        :param remind: 提醒词
        :param background_image: 背景图片
        :return:
        """

    def right_image_left_text_display_process(self, title, image, text, remind, background_image):
        """
        右图左文显示
        :param title: 标题
        :param image: 图片
        :param text: 文字
        :param remind: 提醒词
        :param background_image: 背景图片
        :return:
        """