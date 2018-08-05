# -*- coding: utf-8 -*-

import os
import sys
import datetime
import wxversion
wxversion.select("2.8-unicode")
import wx
sys.path.append('/home/pi/xiaolan/')
from Base import xiaolanBase

class BaseDisplay(xiaolanBase):

    def __init__(self):

        super(BaseDisplay, self).__init__()
        from ButtonProcess import ButtonProcess
        self.button_process = ButtonProcess()
        self.app = wx.App()
        self.SetPosition(wx.Point(0, 0))
        self.window = wx.Frame(None, title = "Xiaolan-V2.0", size = (1024, 600))
        c_x, c_y, c_w, c_h = wx.ClientDisplayRect()
        self.window.SetSize(wx.Size(c_w, c_h))
        self.panel = wx.Panel(window)


    def main_page_display_process(self):

        """
        主页显示
        :return:
        """
        # 背景图片
        image = wx.Image('/home/pi/xiaolan/memory_center/display_img/main_page_background_image.png',
                         wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        wx.StaticBitmap(self, 1, image, (0, 0))

        # 时间显示
        now_time = datetime.datetime.now().strftime('%H:%M')
        Wx.StaticText(self.panel, 2, label=now_time, position=(30, 100), size=(100, 200), style=wx.ALIGN_CENTER)

        # 勿扰模式按钮
        sleep_mode_icon = wx.Bitmap('/home/pi/xiaolan/memory_center/display_img/sleep_icon.png', wx.BITMAP_TYPE_PNG)
        sleep_mode_button = wx.BitmapButton(self.panel, id=3, bitmap=sleep_mode_icon, pos=(924, 100), size=(70, 70))
        sleep_mode_button.Bind(wx.EVT_BUTTON, self.button_process.sleep_mode_button_process)

        # 技能中心按钮
        skill_center_icon = wx.Bitmap('/home/pi/xiaolan/memory_center/display_img/skill_center_icon.png', wx.BITMAP_TYPE_PNG)
        skill_center_button = wx.BitmapButton(self.panel, id=4, bitmap=skill_center_icon, pos=(839, 100), size=(70, 70))
        skill_center_button.Bind(wx.EVT_BUTTON, self.button_process.skill_center_button_process)

        # 小蓝设置按钮
        xiaolan_setting_icon = wx.Bitmap('/home/pi/xiaolan/memory_center/display_img/setting_icon.png', wx.BITMAP_TYPE_PNG)
        xiaolan_setting_button = wx.BitmapButton(self.panel, id=5, bitmap=xiaolan_setting_icon, pos=(754, 100), size=(70, 70))
        xiaolan_setting_button.Bind(wx.EVT_BUTTON, self.button_process.xiaolan_setting_button_process)



    def recording_display_process(self):

        """
        录制音频显示
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