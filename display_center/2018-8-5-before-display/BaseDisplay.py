# -*- coding: utf-8 -*-

import os
import sys
import datetime
import wxversion
wxversion.select("2.8-unicode")
import wx
sys.path.append('/home/pi/xiaolan/')
from Base import xiaolanBase

class BaseDisplay(wx.Frame):

    def __init__(self):

        """
        展示基类
        """
        super(BaseDisplay, self).__init__()
        self.frame = wx.Frame(self, None, -1, "Xiaolan-V2.0-MainPage", (0, 0), size = (1024, 600))

        from ButtonProcess import ButtonProcess
        self.button_process = ButtonProcess()
        self.xiaolan_base = xiaolanBase()

    def update(self, type):

        """
        更新
        :param type: 类型
        :return:
        """
        self.frame.Show(False)
        if type == 'MainPage':
            self.frame = MainPageDisplay()
        elif type == 'Recording':
            self.frame = RecordingDisplay()
        elif type == 'WeatherPage':
            self.frame = WeatherPage()
        elif type == 'RecommendPage':
            self.frame = ReaommendPage()
        else:
            self.frame = MainPageDisplay()
        self.frame.Show(True)

class MainPageDisplay(wx.Frame):

    def __init__(self):

        """
        小蓝主页展示
        """
        super(XiaolanDisplay, self).__init__()
        wx.Frame.__init__(self, None, -1, title='Xiaolan-V2.0MainPage', size=(1024, 600), pos=(0, 0))
        self.main_page_display_process()

    def main_page_display_process(self):

        """
        主页
        :return:
        """
        panel = wx.Panel(self)
        image = wx.Image('/home/pi/xiaolan/memory_center/display_img/main_page_background_image.png',
                         wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        wx.StaticBitmap(panel, 1, image, (0, 0))

        # 时间显示
        now_time = datetime.datetime.now().strftime('%H:%M')
        Wx.StaticText(panel, 2, label=now_time, position=(30, 100), size=(100, 200), style=wx.ALIGN_CENTER)

        # 勿扰模式按钮
        sleep_mode_icon = wx.Bitmap('/home/pi/xiaolan/memory_center/display_img/sleep_icon.png', wx.BITMAP_TYPE_PNG)
        sleep_mode_button = wx.BitmapButton(panel, id=3, bitmap=sleep_mode_icon, pos=(924, 100), size=(70, 70))
        sleep_mode_button.Bind(wx.EVT_BUTTON, self.button_process.sleep_mode_button_process)

        # 技能中心按钮
        skill_center_icon = wx.Bitmap('/home/pi/xiaolan/memory_center/display_img/skill_center_icon.png',
                                      wx.BITMAP_TYPE_PNG)
        skill_center_button = wx.BitmapButton(panel, id=4, bitmap=skill_center_icon, pos=(839, 100),
                                              size=(70, 70))
        skill_center_button.Bind(wx.EVT_BUTTON, self.button_process.skill_center_button_process)

        # 小蓝设置按钮
        xiaolan_setting_icon = wx.Bitmap('/home/pi/xiaolan/memory_center/display_img/setting_icon.png',
                                         wx.BITMAP_TYPE_PNG)
        xiaolan_setting_button = wx.BitmapButton(panel, id=5, bitmap=xiaolan_setting_icon, pos=(754, 100),
                                                 size=(70, 70))
        xiaolan_setting_button.Bind(wx.EVT_BUTTON, self.button_process.xiaolan_setting_button_process)

        # 提醒词
        remind = '小蓝同学，你会干什么'
        Wx.StaticText(panel, 2, label=remind, position=(362, 540), size=(50, 300), style=wx.ALIGN_CENTER)


class RecordingDisplay(wx.Frame):

    def __init__(self):

        """
        小蓝录音展示
        """
        super(XiaolanDisplay, self).__init__()
        wx.Frame.__init__(self, None, -1, title='Xiaolan-V2.0RecordingPage', size=(1024, 600), pos=(0, 0))
        self.recording_display_process()

    def recording_display_process(self):

        """
        录制音频显示
        :return:
        """
        panel = wx.Panel(self)
        image = wx.Image('/home/pi/xiaolan/memory_center/display_img/main_page_background_image_recording.png',
                         wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        wx.StaticBitmap(panel, 1, image, (0, 0))
        # 时间显示
        now_time = datetime.datetime.now().strftime('%H:%M')
        Wx.StaticText(panel, 2, label=now_time, position=(30, 100), size=(100, 200), style=wx.ALIGN_CENTER)

        # 勿扰模式按钮
        sleep_mode_icon = wx.Bitmap('/home/pi/xiaolan/memory_center/display_img/sleep_icon.png', wx.BITMAP_TYPE_PNG)
        sleep_mode_button = wx.BitmapButton(panel, id=3, bitmap=sleep_mode_icon, pos=(924, 100), size=(70, 70))
        sleep_mode_button.Bind(wx.EVT_BUTTON, self.button_process.sleep_mode_button_process)

        # 技能中心按钮
        skill_center_icon = wx.Bitmap('/home/pi/xiaolan/memory_center/display_img/skill_center_icon.png',
                                      wx.BITMAP_TYPE_PNG)
        skill_center_button = wx.BitmapButton(panel, id=4, bitmap=skill_center_icon, pos=(839, 100),
                                              size=(70, 70))
        skill_center_button.Bind(wx.EVT_BUTTON, self.button_process.skill_center_button_process)

        # 小蓝设置按钮
        xiaolan_setting_icon = wx.Bitmap('/home/pi/xiaolan/memory_center/display_img/setting_icon.png',
                                         wx.BITMAP_TYPE_PNG)
        xiaolan_setting_button = wx.BitmapButton(panel, id=5, bitmap=xiaolan_setting_icon, pos=(754, 100),
                                                 size=(70, 70))
        xiaolan_setting_button.Bind(wx.EVT_BUTTON, self.button_process.xiaolan_setting_button_process)

class WeatherPage(wx.Frame):

    def __init__(self):

        """
        小蓝天气页面展示
        """
        super(WeatherPage, self).__init__()
        wx.Frame.__init__(self, None, -1, title='Xiaolan-V2.0WeatherPage', size=(1024, 600), pos=(0, 0))
        self.wather_page_display_process()

    def wather_page_display_process(self):

        """
        天气页展示
        :return:
        """

class ReaommendPage(wx.Frame):

    def __init__(self):

        super(ReaommendPage, self).__init__()
        wx.Frame.__init__(self, None, -1, title='Xiaolan-V2.0WeatherPage', size=(1024, 600), pos=(0, 0))
        self.recommend_page_display_process()

    def recommend_page_display_process(self):

        """
        推荐页展示
        :return:
        """