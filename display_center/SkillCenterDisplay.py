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

class SkillCenterPage(QWidget, xiaolanBase):

    def __init__(self):

        super(SkillCenterPage, self).__init__()
        self.skill_center_page_display()

    def skill_center_page_display(self):

        """
        技能中心页面
        :return:
        """
        self.set_skill_center_background_image()
        self.set_recommend_skill()

    def set_recommend_skill(self):

        """
        设置推荐技能
        :return:
        """
        recommend_skill = self.client_to_server('get_recommend_skill', 0)
        turn = 1
        we = 30
        hi = 30
        long = len(recommend_skill)
        while 1 == 1:
            if turn == long + 1:
                break
            else:
                requests.get(recommend_skill[turn])
                with open(r"/home/pi/xiaolan/memory_center/display_image/skill_recommend_image.png", 'wb') as f:
                    r.raw.decode_content = True
                    shutil.copyfileobj(r.raw, f)

                skill_button = QPushButton("", self)
                skill_button.move(744, 50)
                sskill_button.pushButton.setStyleSheet('QPushButton{border-image:url(/home/pi/xiaolan/memory_center/display_image/skill_recommend_image.png)}')
                button.clicked.connect(self.skill_page_display)
                skill_button.move(we, hi)

                f = open('/home/pi/xiaolan/memory_center/more/recommend_skill', 'w')
                f.write(recommend_skill[turn])
                f.close()

                turn += 1
                hi += 60

    def skill_page_display(self):

        """
        技能介绍页面
        :return:
        """

    def set_skill_center_background_image(self):

        """
        设置技能中心背景图片
        :return:
        """
        palette = QtGui.QPalette(self)
        palette.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap(image_path)))
        self.setPalette(palette)

    def set_skill_page_background_image(self):

        """
        设置技能介绍页面背景图片
        :return:
        """